/**
 * Accounts API - Index
 * User authentication and profile management
 * 
 * Zone: accounts
 * Apps: apps.users
 */

export * from './sdk.gen';
export * from './types.gen';
export * from './client.gen';

// Re-export main client for convenience
export { client as default } from './client.gen'; 