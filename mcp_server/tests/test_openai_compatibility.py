"""Unit tests for OpenAI-compatible endpoint handling in factories."""

import pytest

from config.schema import EmbedderConfig, LLMConfig, OpenAIProviderConfig
from services import factories


class DummyAsyncOpenAI:
    """Capture constructor arguments for assertions."""

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class DummyOpenAIClient:
    """Test double for graphiti OpenAIClient."""

    def __init__(self, config=None, client=None, reasoning=None, verbosity=None, **kwargs):
        self.config = config
        self.client = client
        self.reasoning = reasoning
        self.verbosity = verbosity
        self.kwargs = kwargs


class DummyOpenAIEmbedder:
    """Test double for graphiti OpenAIEmbedder."""

    def __init__(self, config=None, client=None, **kwargs):
        self.config = config
        self.client = client
        self.kwargs = kwargs


def _build_llm_config(api_key: str | None, api_url: str | None) -> LLMConfig:
    llm_config = LLMConfig(provider='openai', model='gpt-4.1-mini')
    llm_config.providers.openai = OpenAIProviderConfig(
        api_key=api_key,
        api_url=api_url,
        organization_id='org-test',
    )
    return llm_config


def _build_embedder_config(api_key: str | None, api_url: str | None) -> EmbedderConfig:
    embedder_config = EmbedderConfig(provider='openai', model='text-embedding-3-small')
    embedder_config.providers.openai = OpenAIProviderConfig(
        api_key=api_key,
        api_url=api_url,
        organization_id='org-test',
    )
    return embedder_config


def test_normalize_openai_base_url():
    assert factories._normalize_openai_base_url('http://127.0.0.1:11434') == 'http://127.0.0.1:11434/v1'
    assert (
        factories._normalize_openai_base_url('https://api.openai.com/v1')
        == 'https://api.openai.com/v1'
    )
    assert factories._normalize_openai_base_url(None) is None


def test_openai_llm_factory_allows_local_endpoint_without_api_key(monkeypatch):
    monkeypatch.setattr(factories, 'OpenAIClient', DummyOpenAIClient)

    import openai

    monkeypatch.setattr(openai, 'AsyncOpenAI', DummyAsyncOpenAI)

    llm_config = _build_llm_config(api_key=None, api_url='http://localhost:11434')
    client = factories.LLMClientFactory.create(llm_config)

    assert isinstance(client, DummyOpenAIClient)
    assert client.config.api_key == 'ollama'
    assert client.config.base_url == 'http://localhost:11434/v1'
    assert client.client.kwargs['organization'] == 'org-test'


def test_openai_llm_factory_requires_api_key_for_non_local_endpoint():
    llm_config = _build_llm_config(api_key=None, api_url='https://api.openai.com/v1')

    with pytest.raises(ValueError, match='OpenAI API key is not configured'):
        factories.LLMClientFactory.create(llm_config)


def test_openai_embedder_factory_supports_local_endpoint_without_api_key(monkeypatch):
    monkeypatch.setattr(factories, 'OpenAIEmbedder', DummyOpenAIEmbedder)

    import openai

    monkeypatch.setattr(openai, 'AsyncOpenAI', DummyAsyncOpenAI)

    embedder_config = _build_embedder_config(api_key=None, api_url='http://127.0.0.1:11434')
    embedder = factories.EmbedderFactory.create(embedder_config)

    assert isinstance(embedder, DummyOpenAIEmbedder)
    assert embedder.config.api_key == 'ollama'
    assert embedder.config.base_url == 'http://127.0.0.1:11434/v1'
    assert embedder.client.kwargs['organization'] == 'org-test'
