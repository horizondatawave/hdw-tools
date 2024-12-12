from crewai_tools import BaseTool  # type: ignore
from hdw_tools.core.base import APIClient
from hdw_tools.core.models import *
from typing import Type
from pydantic import BaseModel


class GetLinkedInCompany(BaseTool):
    name: str = "Get LinkedIn company"
    description: str = "Get LinkedIn company"
    args_schema: Type[BaseModel] = LinkedinCompanyPayload

    def _run(self, **kwargs: dict) -> list[LinkedinCompany] | dict:
        client = APIClient()
        return client.get_data(endpoint="linkedin/company", request_payload=kwargs, response_model=LinkedinCompany)


class GetLinkedInCompanyPosts(BaseTool):
    name: str = "Get LinkedIn company posts"
    description: str = "Get LinkedIn company posts"
    args_schema: Type[BaseModel] = LinkedinCompanyPostsPayload

    def _run(self, **kwargs: dict) -> list[LinkedinUserPost] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/company/posts", request_payload=kwargs, response_model=LinkedinUserPost
        )


class GetLinkedInGroup(BaseTool):
    name: str = "Get LinkedIn group"
    description: str = "Get LinkedIn group"
    args_schema: Type[BaseModel] = LinkedinGroupPayload

    def _run(self, **kwargs: dict) -> list[LinkedinGroup] | dict:
        client = APIClient()
        return client.get_data(endpoint="linkedin/group", request_payload=kwargs, response_model=LinkedinGroup)


class GetLinkedInPost(BaseTool):
    name: str = "Get LinkedIn post"
    description: str = "Get LinkedIn post"
    args_schema: Type[BaseModel] = LinkedinPostPayload

    def _run(self, **kwargs: dict) -> list[LinkedinUserPost] | dict:
        client = APIClient()
        return client.get_data(endpoint="linkedin/post", request_payload=kwargs, response_model=LinkedinUserPost)


class GetLinkedInPostComments(BaseTool):
    name: str = "Get LinkedIn post comments"
    description: str = "Get LinkedIn post comments"
    args_schema: Type[BaseModel] = LinkedinPostCommentsPayload

    def _run(self, **kwargs: dict) -> list[LinkedinPostComment] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/post/comments", request_payload=kwargs, response_model=LinkedinPostComment
        )


class GetLinkedInPostReactions(BaseTool):
    name: str = "Get LinkedIn post reactions"
    description: str = "Get LinkedIn post reactions"
    args_schema: Type[BaseModel] = LinkedinPostReactionsPayload

    def _run(self, **kwargs: dict) -> list[LinkedinPostReaction] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/post/reactions", request_payload=kwargs, response_model=LinkedinPostReaction
        )


class SearchLinkedInCompanies(BaseTool):
    name: str = "Search LinkedIn companies"
    description: str = "Search LinkedIn companies"
    args_schema: Type[BaseModel] = LinkedinSearchCompaniesPayload

    def _run(self, **kwargs: dict) -> list[LinkedinSearchCompany] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/search/companies", request_payload=kwargs, response_model=LinkedinSearchCompany
        )


class SearchLinkedInEducations(BaseTool):
    name: str = "Search LinkedIn educations"
    description: str = "Search LinkedIn educations"
    args_schema: Type[BaseModel] = LinkedinSearchEducationsPayload

    def _run(self, **kwargs: dict) -> list[LinkedinSearchEducation] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/search/educations",
            request_payload=kwargs,
            response_model=LinkedinSearchEducation,
        )


class SearchLinkedinIndustries(BaseTool):
    name: str = "Search LinkedIn industries"
    description: str = "Search LinkedIn industries"
    args_schema: Type[BaseModel] = LinkedinSearchIndustriesPayload

    def _run(self, **kwargs: dict) -> list[LinkedinSearchIndustry] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/search/industries",
            request_payload=kwargs,
            response_model=LinkedinSearchIndustry,
        )


class SearchLinkedinJobs(BaseTool):
    name: str = "Search LinkedIn jobs"
    description: str = "Search LinkedIn jobs"
    args_schema: Type[BaseModel] = LinkedinSearchJobsPayload

    def _run(self, **kwargs: dict) -> list[LinkedinSearchJob] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/search/jobs",
            request_payload=kwargs,
            response_model=LinkedinSearchJob,
        )


class SearchLinkedInLocations(BaseTool):
    name: str = "Search LinkedIn locations"
    description: str = "Search LinkedIn locations"
    args_schema: Type[BaseModel] = LinkedinSearchLocationsPayload

    def _run(self, **kwargs: dict) -> list[LinkedinSearchLocation] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/search/locations", request_payload=kwargs, response_model=LinkedinSearchLocation
        )


class SearchLinkedInUsers(BaseTool):
    name: str = "Search LinkedIn users"
    description: str = "Search LinkedIn users"
    args_schema: Type[BaseModel] = LinkedinSearchUsersPayload

    def _run(self, **kwargs: dict) -> list[LinkedinSearchUser] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/search/users", request_payload=kwargs, response_model=LinkedinSearchUser
        )


class GetLinkedInUser(BaseTool):
    name: str = "Get LinkedIn user"
    description: str = "Get LinkedIn user by url or alias"
    args_schema: Type[BaseModel] = LinkedinUserPayload

    def _run(self, **kwargs: dict) -> list[LinkedinUser] | dict:
        client = APIClient()
        return client.get_data(endpoint="linkedin/user", request_payload=kwargs, response_model=LinkedinUser)


class GetLinkedInUserPosts(BaseTool):
    name: str = "Get LinkedIn user posts"
    description: str = "Get LinkedIn user by url or alias"

    def _run(self, urn_value: str, count: int, timeout: int = 300) -> list[LinkedinUserPost] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/user/posts",
            request_payload={"urn": {"type": "fsd_profile", "value": urn_value}, "count": count, "timeout": timeout},
            response_model=LinkedinUserPost,
        )


class GetLinkedInUserReactions(BaseTool, APIClient):
    name: str = "Get LinkedIn user reactions"
    description: str = "Get LinkedIn user reactions"

    def _run(self, urn_value: str, count: int, timeout: int = 300) -> list[LinkedinUserPost] | dict:
        client = APIClient()
        return client.get_data(
            endpoint="linkedin/user/reactions",
            request_payload={"urn": {"type": "fsd_profile", "value": urn_value}, "count": count, "timeout": timeout},
            response_model=LinkedinUserPost,
        )
