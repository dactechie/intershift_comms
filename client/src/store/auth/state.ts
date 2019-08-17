export interface AuthState {
    username: string;
    isLoggedIn: boolean;
}

export interface IAuthCredentials {
    username: string;
    password: string;
    token: string;
}
