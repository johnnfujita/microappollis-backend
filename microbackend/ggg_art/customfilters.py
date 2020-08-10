

# from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
# from .models import Artwork

# class ArtworkFilter(FilterSet):
#     from_release_date = DateTimeFilter(
#         field_name = 'release_date', lookup_expr='gte'
#     )
#     to_release_date = DateTimeFilter(
#         field_name='release_date', lookup_expr='lte'
#     )
#     min_price = NumberFilter(
#         field_name='price', lookup_expr='gte'
#     )
#     max_price = NumberFilter(
#         field_name='price', lookup_expr='lte'
#     )
#     location_name = AllValuesFilter(
#         field_name='displayed_at__name'
#     )
#     artist_name = AllValuesFilter(
#         field_name='artist__name'
#     )

#     class Meta:
#         model = Artwork
#         fields = (
#             'available_original',
#             'min_price',
#             'max_price',
#             'from_release_date',
#             'to_release_date',
#             'artist_name',
#             'location_name'
#         )