from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from django.db.models import FloatField
from django.db.models.functions import Cast

from movies.models import FilmWork
from movies.models import PersonFilmWork


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']

    def aggregate_person(self, role):
        return ArrayAgg('persons__full_name', distinct=True,
                        filter=Q(persons__full_name__isnull=False)
                        & Q(personfilmwork__role=role))

    def get_queryset(self):
        filmworks = FilmWork.objects.all().values(
            'id', 'title', 'description', 'creation_date', 'type'
            ).annotate(
            rating=Cast('rating', output_field=FloatField()),
            genres=ArrayAgg('genres__name', distinct=True),
            actors=self.aggregate_person(PersonFilmWork.Roles.actor),
            directors=self.aggregate_person(PersonFilmWork.Roles.director),
            writers=self.aggregate_person(PersonFilmWork.Roles.writer)
        )
        return filmworks

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.get_context_data())


class MoviesListApi(MoviesApiMixin, BaseListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()

        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            50
        )

        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(page.object_list)
        }

        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):

    def get_context_data(self, *, object_list=None, **kwargs):
        return kwargs['object']
