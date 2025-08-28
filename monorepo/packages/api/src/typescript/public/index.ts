/**
 * Public API - Index
 * Public API for testing - posts and content
 *
 * Zone: public
 * Apps: apps.public_api
 */

export * from "./sdk.gen";
export * from "./types.gen";
export * from "./client.gen";

// Re-export main client for convenience
export { client as default } from "./client.gen";
