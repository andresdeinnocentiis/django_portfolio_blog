import { createRouter, createWebHistory } from 'vue-router'
import { useUserLoggedStore } from '../stores/userLogged'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component:  () => import('../views/HomeView.vue'),
    },
    {
      path: '/login/',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
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
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/posts/',
      name: 'posts',
      component: () => import('../views/PostsView.vue'),
    },
    {
      path: '/posts/:id',
      name: 'project',
      component:  () => import('../views/ProjectView.vue'),
      props: true
    },
    {
      path: '/about/',
      name: 'about',
      component:  () => import('../views/PostsView.vue'),
    },
    {
      path: '/contact/',
      name: 'contact',
      component:  () => import('../views/PostsView.vue'),
    },
  ]
})

export default router
