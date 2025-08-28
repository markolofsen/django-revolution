/**
 * Private API - Index
 * Private API for testing - categories, products, orders
 *
 * Zone: private
 * Apps: apps.private_api
 */

export * from "./sdk.gen";
export * from "./types.gen";
export * from "./client.gen";

// Re-export main client for convenience
export { client as default } from "./client.gen";
