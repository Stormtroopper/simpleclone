import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Home from './pages/Home'
import { Login } from './pages/Login'
import { useSelector } from 'react-redux'
import type { RootState } from './store/store'
import { ProtectedRoute } from './components/ui/ProtectedRoute'
import RestaurantCard from './components/restaurants/RestaurantCard'
import { RestaurantList } from './components/restaurants/RestaurantList'
import { Register } from './pages/Register'
import NotFound from './pages/NotFound'
import { NavBar } from './components/ui/NavBar'
function App() {
  const isAuthenticated=useSelector((state:RootState)=>state.auth.isAuthenticated)
  return (
    <>
    <NavBar isAuthenticated={isAuthenticated}/>
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login isAuthenticated={isAuthenticated} />} />
        <Route path="/register" element={<Register isAuthenticated={isAuthenticated} />} />
        <Route path="/restaurants"element={<ProtectedRoute isAuthenticated={isAuthenticated} >
          <RestaurantCard/>
        </ProtectedRoute>} />
                <Route path="/restaurants-list"element={<ProtectedRoute isAuthenticated={isAuthenticated} >
          <RestaurantList/>
        </ProtectedRoute>} />
        <Route path='*' element={<NotFound/>}/>
      </Routes>
    </Router>
    </>
  )
}

export default App