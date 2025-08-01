#!/usr/bin/env python3
"""
Example usage of the generated Public API client.

This demonstrates how to use the HTTP client with generated models and specific API methods.
"""

import json
from typing import Dict, Any, List
from datetime import datetime

# Import the generated client and models
from .http_client import public_client, PublicClient
from .django_revolution_public import *


def main():
    """Main example function"""
    
    print("🔗 Public API Client Example")
    print("=" * 50)
    
    # Initialize client
    client = public_client("http://localhost:8000")
    
    # Example 1: Basic API calls
    print("\n📋 Example 1: Basic API calls")
    try:
        # GET request example
        print("📡 Making GET request...")
        response = client.get("public/")
        if response.is_success():
            print(f"✅ GET successful: {response.status_code}")
            print(f"📄 Response: {json.dumps(response.data, indent=2)}")
        else:
            print(f"❌ GET failed: {response.status_code}")
            
    except Exception as e:
        print(f"⚠️  Server not running or error: {e}")
    
    # Example 2: Using generated models
    print("\n📋 Example 2: Using generated models")
    try:
        # Create model instances (adjust based on your actual models)
        # Example: Create a post request
        if 'Post' in globals():
            # Create a user first
            user = User(
                id=1,
                username="testuser",
                email="test@example.com",
                first_name="Test",
                last_name="User",
                date_joined=datetime.now()
            )
            
            # Create a post
            post = Post(
                id=1,
                title="Test Post",
                content="Test content",
                author=user,
                author_id=1,
                published=True,
                created_at=datetime.now()
            )
            print(f"✅ Created model: {post.title}")
            
    except Exception as e:
        print(f"⚠️  Model example error: {e}")
    
    # Example 3: Specific API Methods
    print("\n📋 Example 3: Specific API Methods")
    try:
        # Get all posts
        print("📡 Getting all posts...")
        response = client.get_posts(ordering="-created_at", page=1)
        if response.is_success():
            print(f"✅ Got posts: {len(response.data.get('results', []))} posts")
        else:
            print(f"❌ Failed to get posts: {response.status_code}")
        
        # Get published posts only
        print("📡 Getting published posts...")
        response = client.get_published_posts(ordering="-created_at")
        if response.is_success():
            print(f"✅ Got published posts: {len(response.data.get('results', []))} posts")
        else:
            print(f"❌ Failed to get published posts: {response.status_code}")
        
        # Create a new post
        print("📡 Creating a new post...")
        post_data = {
            "title": "New Post via Client",
            "content": "This post was created using the API client",
            "author_id": 1,
            "published": False
        }
        response = client.create_post(post_data)
        if response.is_success():
            print(f"✅ Created post: {response.data.get('title')}")
            post_id = response.data.get('id')
            
            # Publish the post
            print(f"📡 Publishing post {post_id}...")
            response = client.publish_post(post_id)
            if response.is_success():
                print(f"✅ Published post {post_id}")
            else:
                print(f"❌ Failed to publish post: {response.status_code}")
                
        else:
            print(f"❌ Failed to create post: {response.status_code}")
            
    except Exception as e:
        print(f"⚠️  Specific API methods error: {e}")
    
    # Example 4: Authentication
    print("\n📋 Example 4: Authentication")
    try:
        # Set auth token
        client.set_auth_token("your-auth-token-here")
        print("✅ Auth token set")
        
        # Make authenticated request
        response = client.get("public/protected-endpoint/")
        if response.is_success():
            print(f"✅ Authenticated request successful")
        else:
            print(f"❌ Authenticated request failed: {response.status_code}")
            
        # Clear auth token
        client.clear_auth_token()
        print("✅ Auth token cleared")
        
    except Exception as e:
        print(f"⚠️  Auth example error: {e}")
    
    # Example 5: Error handling
    print("\n📋 Example 5: Error handling")
    try:
        # Make request that might fail
        response = client.get("public/non-existent-endpoint/")
        if response.is_success():
            print("✅ Request successful")
        else:
            print(f"❌ Request failed as expected: {response.status_code}")
            
    except Exception as e:
        print(f"✅ Caught expected error: {e}")
    
    # Example 6: Advanced usage with specific methods
    print("\n📋 Example 6: Advanced usage with specific methods")
    try:
        # Get posts by author
        print("📡 Getting posts by author...")
        response = client.get_posts_by_author(author_id=1)
        if response.is_success():
            print(f"✅ Got posts by author: {len(response.data.get('results', []))} posts")
        else:
            print(f"❌ Failed to get posts by author: {response.status_code}")
        
        # Update a post
        print("📡 Updating a post...")
        update_data = {
            "title": "Updated Post Title",
            "content": "Updated content"
        }
        response = client.patch_post(post_id=1, post_data=update_data)
        if response.is_success():
            print(f"✅ Updated post: {response.data.get('title')}")
        else:
            print(f"❌ Failed to update post: {response.status_code}")
            
    except Exception as e:
        print(f"⚠️  Advanced usage error: {e}")
    
    print("\n🎉 Example completed!")


if __name__ == "__main__":
    main() 