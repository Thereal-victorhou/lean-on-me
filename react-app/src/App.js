import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import DailyNutritionGoals from './components/Daily_Nutrition_Goals';
import FoodLog from './components/Food_Log';
import Navigation from './components/Splash/Navigation';
import Splash from './components/Splash/Splash';
import Home from './components/Home/Home';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      {/* <NavBar /> */}
      <Switch>
        <Route path='/login' exact={true}>
          <Navigation />
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <Navigation />
          <SignUpForm />
        </Route>
        <Route path='/' exact={true} >
          <Navigation />
          <Splash />
        </Route>
        <Route path='/home' exact={true}>
          <Navigation />
          <Home />
        </Route>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <Route path='/daily-nutrition-goals' exact={true}>
          <Navigation />
          <DailyNutritionGoals />
        </Route>
        <Route path='/food-log' exact={true}>
          <Navigation />
          <FoodLog />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
