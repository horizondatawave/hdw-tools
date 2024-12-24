from llama_index.core.tools.tool_spec.base import BaseToolSpec
from hdw_tools.core.base import APIClient
from hdw_tools.core.models import *


class LinkedInToolSpec(BaseToolSpec):
    spec_functions = [
        "linkedin_company",
        "linkedin_company_employees",
        "linkedin_company_posts",
        "linkedin_email_user",
        "linkedin_group",
        "linkedin_post",
        "linkedin_post_comments",
        "linkedin_post_reactions",
        "linkedin_search_companies",
        "linkedin_search_educations",
        "linkedin_search_industries",
        "linkedin_search_jobs",
        "linkedin_search_locations",
        "linkedin_search_users",
        "linkedin_user",
        "linkedin_user_endorsers",
        "linkedin_user_posts",
        "linkedin_user_reactions",
    ]

    def __init__(self) -> None:
        self.client = APIClient()

    def linkedin_company(self, request_payload: LinkedinCompanyPayload) -> list[LinkedinCompany] | dict:
        """
        Retrieve detailed information about a LinkedIn company by URL or alias.
        Endpoint: "linkedin/company"
        IMPORTANT: Use this tool to fetch company-specific data such as name, description, industry, and other relevant details.

        :return: A list of dictionaries containing company details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/company", request_payload=request_payload, response_model=LinkedinCompany
        )

    def linkedin_company_employees(
        self, request_payload: LinkedinCompanyEmployeesPayload
    ) -> list[LinkedinCompanyEmployee] | dict:
        """
        Retrieve a list of employees working for a LinkedIn company identified by URN.
        Endpoint: "linkedin/company/employees"
        IMPORTANT: Use this tool to fetch details about employees associated with a specific company. Ensure that a valid company URN is included in the request payload.

        :return: A list of dictionaries containing the details of company employees, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/company/employees",
            request_payload=request_payload,
            response_model=LinkedinCompanyEmployee,
        )

    def linkedin_company_posts(self, request_payload: LinkedinCompanyPostsPayload) -> list[LinkedinUserPost] | dict:
        """
        Retrieve posts published by a LinkedIn company URN.
        Endpoint: "linkedin/company/posts"
        IMPORTANT: Use this tool to fetch recent posts or updates shared by a specific company. Ensure that a valid company URN is included in the request payload.

        :return: A list of dictionaries containing the details of company posts, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/company/posts", request_payload=request_payload, response_model=LinkedinUserPost
        )

    def linkedin_group(self, request_payload: LinkedinGroupPayload) -> list[LinkedinGroup] | dict:
        """
        Retrieve detailed information about a LinkedIn group by its URN or URL.
        Endpoint: "linkedin/group"
        IMPORTANT: Use this tool to fetch group-specific data such as name, description, member count, and other relevant details. Ensure that a valid group URN is provided in the request payload.

        :return: A list of dictionaries containing group details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/group", request_payload=request_payload, response_model=LinkedinGroup
        )

    def linkedin_email_user(self, request_payload: LinkedinEmailUserPayload) -> list[LinkedinEmailUser] | dict:
        """
        Retrieve detailed information about a LinkedIn user by their email address.
        Endpoint: "linkedin/email/user"
        IMPORTANT: Use this tool to fetch user-specific data such as name, profile, connections, and other relevant details by providing a valid email address in the request payload.

        :return: A list of dictionaries containing user details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/email/user", request_payload=request_payload, response_model=LinkedinEmailUser
        )

    def linkedin_post(self, request_payload: LinkedinPostPayload) -> list[LinkedinUserPost] | dict:
        """
        Never use alias as value. use only URN.
        Retrieve detailed information about a specific LinkedIn post by its URN.
        Endpoint: "linkedin/post"
        IMPORTANT: Use this tool to fetch post-specific data such as content, author details, reactions, and other relevant metadata. Ensure that a valid post URN is provided in the request payload.

        :return: A list of dictionaries containing post details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/post", request_payload=request_payload, response_model=LinkedinUserPost
        )

    def linkedin_post_comments(self, request_payload: LinkedinPostCommentsPayload) -> list[LinkedinPostComment] | dict:
        """
        Never use alias as value. use only URN from linkedin_company tool.
        Endpoint: "linkedin/post/comments"
        IMPORTANT: Use this tool to fetch the comments associated with a specific post. Ensure that a valid post URN is included in the request payload for accurate results.

        :return: A list of dictionaries containing comment details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/post/comments", request_payload=request_payload, response_model=LinkedinPostComment
        )

    def linkedin_post_reactions(
        self, request_payload: LinkedinPostReactionsPayload
    ) -> list[LinkedinPostReaction] | dict:
        """
        Retrieve reactions on a specific LinkedIn post by its URN.
        Endpoint: "linkedin/post/reactions"
        IMPORTANT: Use this tool to fetch reactions (likes, emojis, etc.) associated with a specific post. Ensure that a valid post URN is provided in the request payload.

        :return: A list of dictionaries containing reaction details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/post/reactions", request_payload=request_payload, response_model=LinkedinPostReaction
        )

    def linkedin_search_companies(
        self, request_payload: LinkedinSearchCompaniesPayload
    ) -> list[LinkedinSearchCompany] | dict:
        """
        Search for LinkedIn companies.

        :param request_payload:
            request_payload.location: Need use the linkedin_search_locations tool to get the location URN.
            request_payload.industry: Need use the linkedin_search_industries tool to get the industry URN.

        :return: A list of dictionaries containing the companies info, or None if not found.
        """
        return self.client.get_data(
            endpoint="linkedin/search/companies", request_payload=request_payload, response_model=LinkedinSearchCompany
        )

    def linkedin_search_educations(
        self, request_payload: LinkedinSearchEducationsPayload
    ) -> list[LinkedinSearchEducation] | dict:
        """
        Search for LinkedIn education URNs by name.
        Endpoint: "linkedin/search/educations"
        IMPORTANT: Always run this tool when you need an education URN for searching users or institutions. This ensures accurate and valid URN retrieval.

        :return: A list of dictionaries containing the education URNs and names, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/search/educations",
            request_payload=request_payload,
            response_model=LinkedinSearchEducation,
        )

    def linkedin_search_industries(
        self, request_payload: LinkedinSearchIndustriesPayload
    ) -> list[LinkedinSearchIndustry] | dict:
        """
        Search for LinkedIn industry URNs by name.
        Endpoint: "linkedin/search/industries"
        IMPORTANT: Always run this tool when you need an industry URN for searching users or companies. This ensures accurate and valid URN retrieval.

        :return: A list of dictionaries containing the industry URNs and names, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/search/industries",
            request_payload=request_payload,
            response_model=LinkedinSearchIndustry,
        )

    def linkedin_search_jobs(self, request_payload: LinkedinSearchJobsPayload) -> list[LinkedinSearchJob] | dict:
        """
        Search for LinkedIn jobs.

        :param request_payload:
            request_payload.industry: Need use the linkedin_search_industries tool to get the industry URN.
            request_payload.company: Need use the linkedin_search_companies tool to get the company URN.

        :return: A list of dictionaries containing the jobs info, or None if not found.
        """
        return self.client.get_data(
            endpoint="linkedin/search/jobs", request_payload=request_payload, response_model=LinkedinSearchJob
        )

    def linkedin_search_locations(
        self, request_payload: LinkedinSearchLocationsPayload
    ) -> list[LinkedinSearchLocation] | dict:
        """
        Search for LinkedIn location URNs by name.
        Endpoint: "linkedin/search/locations"
        IMPORTANT: Always run this tool first when you need a location URN for searching users or companies. This ensures accurate and valid URN retrieval.

        :return: A list of dictionaries containing the location URNs and names, or a dictionary with the response from endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/search/locations", request_payload=request_payload, response_model=LinkedinSearchLocation
        )

    def linkedin_search_users(self, request_payload: LinkedinSearchUsersPayload) -> list[LinkedinSearchUser] | dict:
        """
        Search for LinkedIn users.

        :param request_payload:
            request_payload.current_company: Need use the linkedin_search_companies tool to get the company URN.
            request_payload.past_company: Need use the linkedin_search_companies tool to get the company URN.
            request_payload.location: Need use the linkedin_search_locations tool to get the location URN.
            request_payload.industry: Need use the linkedin_search_industries tool to get the industry URN.
            request_payload.education: Need use the linkedin_search_educations tool to get the education URN.

        :return: A list of dictionaries containing the users info, or None if not found.
        """

        return self.client.get_data(
            endpoint="linkedin/search/users", request_payload=request_payload, response_model=LinkedinSearchUser
        )

    def linkedin_user(self, request_payload: LinkedinUserPayload) -> list[LinkedinUser] | dict:
        """
        Retrieve detailed information about a LinkedIn user by their URN or alias or URL.
        Endpoint: "linkedin/user"
        IMPORTANT: Use this tool to fetch user-specific data such as name, profile, connections, and other relevant details. Ensure that a valid user URN is provided in the request payload.

        :return: A list of dictionaries containing user details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/user", request_payload=request_payload, response_model=LinkedinUser
        )

    def linkedin_user_endorsers(self, request_payload: LinkedinUserURNPayload) -> list[LinkedinUserEndorser] | dict:
        """
        Retrieve the list of endorsers for a specific LinkedIn user URN.
        Endpoint: "linkedin/user/endorsers"
        IMPORTANT: Ensure that a valid user URN is provided in the request payload for accurate results.

        :return: A list of dictionaries containing endorser details, or a dictionary with the response from the endpoint.
        """

        return self.client.get_data(
            endpoint="linkedin/user/endorsers", request_payload=request_payload, response_model=LinkedinUserEndorser
        )

    def linkedin_user_posts(self, request_payload: LinkedinUserURNPayload) -> list[LinkedinUserPost] | dict:
        """
        Never use alias as value. use only URN from linkedin_user tool.
        :return: A list of dictionaries containing post details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/user/posts", request_payload=request_payload, response_model=LinkedinUserPost
        )

    def linkedin_user_reactions(self, request_payload: LinkedinUserURNPayload) -> list[LinkedinUserPost] | dict:
        """
        Retrieve reactions on posts made by a specific LinkedIn user URN.
        Endpoint: "linkedin/user/reactions"
        IMPORTANT: Ensure that a valid user URN is provided in the request payload for accurate results.

        :return: A list of dictionaries containing reaction details, or a dictionary with the response from the endpoint.
        """
        return self.client.get_data(
            endpoint="linkedin/user/reactions", request_payload=request_payload, response_model=LinkedinUserPost
        )
