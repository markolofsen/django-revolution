/**
 * Account Types - Re-exported from generated API
 * Clean type definitions for authentication and user management
 */

import { AccountsTypes } from '@repo/api';

// Simple aliases for cleaner code
export type UserProfile = AccountsTypes.UserProfile;
export type UserRegistration = AccountsTypes.UserCreate;
export type TokenRefresh = AccountsTypes.TokenRefreshWritable;

// Basic auth types
export interface LoginCredentials {
    email: string;
    password: string;
}

// Context interface
export interface AuthContextType {
  // State
  user: UserProfile | null;
  isLoading: boolean;
  isAuthenticated: boolean;
  error: string | null;
  
  // Auth Functions
  register: (userData: UserRegistration) => Promise<boolean>;
  login: (credentials: LoginCredentials) => Promise<boolean>;
  logout: () => Promise<void>;
  refreshToken: () => Promise<boolean>;
  
  // User Functions
  updateProfile: (profileData: Partial<UserProfile>) => Promise<boolean>;
  getCurrentUser: () => Promise<void>;
  
  // Utility Functions
  clearError: () => void;
}

// Provider props
export interface AuthProviderProps {
  children: React.ReactNode;
} 