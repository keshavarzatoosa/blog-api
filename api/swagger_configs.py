from functools import partial
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import BlogPostSerializer

base_swagger = partial(
    swagger_auto_schema,
    )

get_list_swagger = base_swagger(
            operation_description="Get a list of all blog posts",
            responses={200: BlogPostSerializer(many=True)}
            )

post_swagger = base_swagger(
            operation_description="Create a new blog post",
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'tags': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                        description="tags",
                        example="['Tech', 'Sport']"
                    ),
                    'categories': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                        description="Enter name of categories",
                        example="['Technology', 'Sport', 'Biology']"
                    ),
                    'title': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Title of blog post",
                        example="This is title"
                    ),
                    'content': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Content of blog post",
                        example="This is Content"
                    ),
                },
                required=['title', 'content']
            ),
            responses={
                201: BlogPostSerializer(),
                400: "Bad request"
                },
            )

get_detail_swagger = base_swagger(
            operation_description="Get a specific blog post by ID",
            responses={
                200: BlogPostSerializer(),
                404: "Not found"
                },
            manual_parameters=[
                openapi.Parameter(
                    name='id',
                    in_=openapi.IN_PATH,
                    description="ID of the blog post",
                    type=openapi.TYPE_INTEGER
                )
            ]
                )

