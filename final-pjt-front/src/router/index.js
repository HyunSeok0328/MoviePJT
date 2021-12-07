import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Community from '@/views/Community.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/Profile.vue'
import Search from '@/views/Search.vue'
import CreateReview from '@/views/CreateReview.vue'
import UpdateReview from '@/views/UpdateReview.vue'
import Review from '@/views/Review.vue'
import Movie from '@/views/Movie.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
  },
  {
    path: '/create',
    name: 'CreateReview',
    component: CreateReview,
  },
  {
    path: '/update/:reviewId',
    name: 'UpdateReview',
    component: UpdateReview,
  },
  {
    path: '/review/:reviewId',
    name: 'Review',
    component: Review,
    props: true,
  },
  {
    path: '/movie/:movieId',
    name: 'Movie',
    component: Movie,
    props: true,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
