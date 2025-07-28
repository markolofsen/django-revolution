// Proxy types from generated API files
// This file re-exports all types from the generated API files for easy access

// Import all types from generated files
import type { PublicTypes } from '@repo/api';
import type { PrivateTypes } from '@repo/api';
import type { AccountsTypes } from '@repo/api';

// Re-export all types for easy access
export {
  PublicTypes,
  PrivateTypes,
  AccountsTypes,
};

// Common type aliases for convenience
export type Post = PublicTypes.Post;
export type PostWritable = PublicTypes.PostWritable;
export type User = PublicTypes.User;
export type PaginatedPostList = PublicTypes.PaginatedPostList;

// Private API types
export type Category = PrivateTypes.Category;
export type Product = PrivateTypes.Product;
export type Order = PrivateTypes.Order;
export type OrderItem = PrivateTypes.OrderItem;
export type StatusEnum = PrivateTypes.StatusEnum;

// Accounts types
export type UserProfile = AccountsTypes.UserProfile;
export type PatchedUserProfile = AccountsTypes.PatchedUserProfile;
export type UserCreate = AccountsTypes.UserCreate;
export type TokenRefresh = AccountsTypes.TokenRefresh;
export type TokenRefreshWritable = AccountsTypes.TokenRefreshWritable;

// API Response types
export type ApiPublicApiPostsListResponse = PublicTypes.ApiPublicApiPostsListResponse;
export type ApiPublicApiPostsCreateResponse = PublicTypes.ApiPublicApiPostsCreateResponse;
export type ApiPublicApiPostsRetrieveResponse = PublicTypes.ApiPublicApiPostsRetrieveResponse;
export type ApiPublicApiPostsUpdateResponse = PublicTypes.ApiPublicApiPostsUpdateResponse;
export type ApiPublicApiPostsPartialUpdateResponse = PublicTypes.ApiPublicApiPostsPartialUpdateResponse;
export type ApiPublicApiPostsDestroyResponse = PublicTypes.ApiPublicApiPostsDestroyResponse;
export type ApiPublicApiPostsPublishCreateResponse = PublicTypes.ApiPublicApiPostsPublishCreateResponse;
export type ApiPublicApiPostsUnpublishCreateResponse = PublicTypes.ApiPublicApiPostsUnpublishCreateResponse;
export type ApiPublicApiPostsByAuthorListResponse = PublicTypes.ApiPublicApiPostsByAuthorListResponse;
export type ApiPublicApiPostsPublishedListResponse = PublicTypes.ApiPublicApiPostsPublishedListResponse;

// API Data types
export type ApiPublicApiPostsListData = PublicTypes.ApiPublicApiPostsListData;
export type ApiPublicApiPostsCreateData = PublicTypes.ApiPublicApiPostsCreateData;
export type ApiPublicApiPostsRetrieveData = PublicTypes.ApiPublicApiPostsRetrieveData;
export type ApiPublicApiPostsUpdateData = PublicTypes.ApiPublicApiPostsUpdateData;
export type ApiPublicApiPostsPartialUpdateData = PublicTypes.ApiPublicApiPostsPartialUpdateData;
export type ApiPublicApiPostsDestroyData = PublicTypes.ApiPublicApiPostsDestroyData;
export type ApiPublicApiPostsPublishCreateData = PublicTypes.ApiPublicApiPostsPublishCreateData;
export type ApiPublicApiPostsUnpublishCreateData = PublicTypes.ApiPublicApiPostsUnpublishCreateData;
export type ApiPublicApiPostsByAuthorListData = PublicTypes.ApiPublicApiPostsByAuthorListData;
export type ApiPublicApiPostsPublishedListData = PublicTypes.ApiPublicApiPostsPublishedListData;
