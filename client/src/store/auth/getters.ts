
import {  AuthState } from './state';

export function getUsername(state: AuthState): string {
      // console.log (" getting usernamne from state ", state);
      return state.username;
  }
