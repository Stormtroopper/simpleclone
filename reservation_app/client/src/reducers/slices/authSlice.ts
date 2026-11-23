import { createSlice,type PayloadAction } from '@reduxjs/toolkit'

interface User {
  id: string
  name: string
  email: string
}

interface AuthState {
  user: User | null
  token: string | null
  isAuthenticated: boolean
}

const initialState: AuthState = {
  isAuthenticated: !!localStorage.getItem('token'),
  user: null,
  token: localStorage.getItem('token'),
}

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    loginSuccess: (state, action: PayloadAction<{ user: User; token: string }>) => {
      state.isAuthenticated = true
      state.user = action.payload.user
      state.token = action.payload.token
      localStorage.setItem('token', action.payload.token)
    },
    loginFailure: (state) => {
      state.isAuthenticated = false
      state.user = null
      state.token = null
      localStorage.removeItem('token')
    },
    logout: (state) => {
      state.isAuthenticated = false
      state.user = null
      state.token = null
      localStorage.removeItem('token')
    },
  },
})

export const { loginSuccess, loginFailure, logout } = authSlice.actions
export default authSlice.reducer