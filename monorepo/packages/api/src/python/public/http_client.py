"""
Public API - HTTP Client
Public API for testing - posts and content

Generated HTTP client for public zone using Django Revolution.
API Prefix: /api/
"""

import json
import logging
from typing import Dict, Any, Optional, List, Union
from pathlib import Path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Import generated models
try:
    from .django_revolution_public import *
except ImportError:
    # Fallback for direct execution
    from django_revolution_public import *

logger = logging.getLogger(__name__)


class PublicConfig:
    """Configuration for PublicClient"""
    
    def __init__(
        self,
        base_url: str = "http://localhost:8000",
        api_prefix: str = "/api/",
        timeout: int = 30,
        max_retries: int = 3,
        headers: Optional[Dict[str, str]] = None,
        auth_token: Optional[str] = None,
    ):
        self.base_url = base_url.rstrip('/')
        self.api_prefix = api_prefix.rstrip('/') + '/'
        self.timeout = timeout
        self.max_retries = max_retries
        self.headers = headers or {}
        self.auth_token = auth_token
        
        # Add auth token to headers if provided
        if auth_token:
            self.headers['Authorization'] = f'Bearer {auth_token}'


class PublicResponse:
    """Response wrapper for API calls"""
    
    def __init__(self, response: requests.Response, data: Any = None):
        self.response = response
        self.data = data
        self.status_code = response.status_code
        self.headers = dict(response.headers)
        self.url = response.url
        
    def is_success(self) -> bool:
        """Check if response was successful"""
        return 200 <= self.status_code < 300
        
    def raise_for_status(self):
        """Raise exception for bad status codes"""
        self.response.raise_for_status()


class PublicClient:
    """HTTP client for public API"""
    
    def __init__(self, config: PublicConfig):
        self.config = config
        self.session = self._create_session()
        
    def _create_session(self) -> requests.Session:
        """Create requests session with retry logic"""
        session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=self.config.max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"],
            backoff_factor=1,
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Set default headers
        session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            **self.config.headers
        })
        
        return session
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> PublicResponse:
        """Make HTTP request to API"""
        url = f"{self.config.base_url}{self.config.api_prefix}{endpoint.lstrip('/')}"
        
        request_headers = {**self.session.headers}
        if headers:
            request_headers.update(headers)
            
        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                headers=request_headers,
                timeout=self.config.timeout
            )
            
            # Parse response data
            response_data = None
            if response.content:
                try:
                    response_data = response.json()
                except json.JSONDecodeError:
                    response_data = response.text
            
            return PublicResponse(response, response_data)
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> PublicResponse:
        """Make GET request"""
        return self._make_request("GET", endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> PublicResponse:
        """Make POST request"""
        return self._make_request("POST", endpoint, data=data)
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> PublicResponse:
        """Make PUT request"""
        return self._make_request("PUT", endpoint, data=data)
    
    def patch(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> PublicResponse:
        """Make PATCH request"""
        return self._make_request("PATCH", endpoint, data=data)
    
    def delete(self, endpoint: str) -> PublicResponse:
        """Make DELETE request"""
        return self._make_request("DELETE", endpoint)
    
    def set_auth_token(self, token: str):
        """Set authentication token"""
        self.config.auth_token = token
        self.session.headers['Authorization'] = f'Bearer {token}'
    
    def clear_auth_token(self):
        """Clear authentication token"""
        self.config.auth_token = None
        if 'Authorization' in self.session.headers:
            del self.session.headers['Authorization']


# Convenience function to create client
def public_client(
    base_url: str = "http://localhost:8000",
    api_prefix: str = "/api/",
    timeout: int = 30,
    max_retries: int = 3,
    headers: Optional[Dict[str, str]] = None,
    auth_token: Optional[str] = None,
) -> PublicClient:
    """Create PublicClient instance"""
    config = PublicConfig(
        base_url=base_url,
        api_prefix=api_prefix,
        timeout=timeout,
        max_retries=max_retries,
        headers=headers,
        auth_token=auth_token,
    )
    return PublicClient(config) 