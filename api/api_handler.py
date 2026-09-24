import requests


class APIHandler:

    def __init__(self, base_url, token=None, timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def find(self, endpoint, response_model=None, validate_schema=True):
        response = self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout
        )
        return self._validate(response, response_model, validate_schema)

    def find_by_id(self, endpoint, resource_id, response_model=None, validate_schema=True):
        return self.find(
            f"{endpoint}/{resource_id}",
            response_model,
            validate_schema
        )

    def create(self, payload, response_model=None):
        data = payload.model_dump() if hasattr(payload, "model_dump") else payload

        response = self.session.post(
            f"{self.base_url}/posts",
            json=data,
            timeout=self.timeout
        )
        return self._validate(response, response_model)

    def put(self, endpoint, resource_id, payload, response_model=None):
        response = self.session.put(
            f"{self.base_url}{endpoint}/{resource_id}",
            json=payload,
            timeout=self.timeout
        )
        return self._validate(response, response_model)

    def delete(self, endpoint, resource_id, response_model=None):
        response = self.session.delete(
            f"{self.base_url}{endpoint}/{resource_id}",
            timeout=self.timeout
        )
        return self._validate(response, response_model)

    def _validate(self, response, model=None, validate_schema=True):
        if validate_schema and model:
            model.model_validate(response.json())

        return response