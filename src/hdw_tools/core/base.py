import requests
from typing import Type
from pydantic import BaseModel
from hdw_tools.core.config import Config


class APIClient:
    def __init__(self) -> None:
        self.config = Config()
        self.headers = {
            "access-token": self.config.HDW_API_KEY,
            "Content-Type": "application/json",
        }

    def get_data[T: BaseModel](
        self,
        endpoint: str,
        method: str = "POST",
        request_payload: BaseModel | dict | None = None,
        params: dict | None = None,
        response_model: Type[T] | None = None,
    ) -> T | list[T] | dict:
        url = f"{self.config.HDW_API_URL}/{endpoint}"

        if isinstance(request_payload, BaseModel):
            request_payload = request_payload.model_dump()

        if request_payload:
            request_payload = {key: value for key, value in request_payload.items() if value}

        res = requests.request(method, url, params=params, json=request_payload, headers=self.headers)

        if not res.ok:
            return {"status_code": res.status_code, "message": res.json()}

        if response_model:
            if isinstance(res.json(), list):
                return [response_model.model_validate(item) for item in res.json()]

            return response_model.model_validate(res.json())

        return res.json()
