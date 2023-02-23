import { createRouter, createWebHistory } from 'vue-router'
import PostsView from '../views/PostsView.vue' 
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ProjectView from '../views/ProjectView.vue'
import { useUserLoggedStore } from '../stores/userLogged'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login/',
      name: 'login',
      component: LoginView,
      beforeEnter: async (to, from, next) => {
        const userLoggedStore = useUserLoggedStore()
        const { isUserLogged } = userLoggedStore

        const isLoggedIn = isUserLogged()
  
        if (isLoggedIn) {
            return next("/");
        }
  
        next();
      },
    },
    {
      path: '/register/',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/posts/',
      name: 'posts',
      component: PostsView
    },
    {
      path: '/posts/:id',
      name: 'project',
      component: ProjectView
    },
    {
      path: '/about/',
      name: 'about',
      component: PostsView
    },
    {
      path: '/contact/',
      name: 'contact',
      component: PostsView
    },
  ]
})

export default router
