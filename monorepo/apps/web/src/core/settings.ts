export const config = {
  // Project information
  project: {
    name: 'Django Revolution',
    description: 'Zero-config TypeScript & Python client generator for Django REST Framework',
    version: '1.0.0',
  },
  
  // External links
  links: {
    github: 'https://github.com/markolofsen/django-revolution',
    developer: 'https://reforms.ai/',
  },
  
  // API configuration
  api: {
    baseUrl: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  },
  
  // SEO defaults
  seo: {
    defaultTitle: 'Django Revolution - Zero-config TypeScript & Python client generator for Django REST Framework',
    defaultDescription: 'Generate fully-typed TypeScript and Python clients for Django REST Framework APIs with zero configuration. Supports OpenAPI, authentication, and more.',
    defaultKeywords: 'django, django rest framework, typescript, python, api client, openapi, code generation, drf',
  },
} as const;

export type Config = typeof config; 