from fastapi import APIRouter

from semantic_matching_interface import query


class AbstractSemanticMatchingInterface:
    """
    Todo
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            "/semantic_matching_service_information",
            self.semantic_matching_service_information,
            methods=["GET"]
        )
        self.router.add_api_route(
            "/semantic_match_objects",
            self.semantic_match_objects,
            methods=["GET"]
        )

    def semantic_matching_service_information(self):
        """
        Information that the Semantic Matching Service can provide about
        itself.
        Should return a `response.SemanticMatchingServiceInformation` object.
        """
        raise NotImplementedError

    def semantic_match_objects(
            self,
            query: query.MatchObjectsQuery
    ):
        """
        A query to match two SubmodelElements semantically.

        Returns a matching score
        """
        raise NotImplementedError
