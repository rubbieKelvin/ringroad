// Composables
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Home.vue"),
      },
      {
        path: "/accounts/signup",
        name: "Signup",
        component: () => import("@/views/auth/Signup.vue"),
      },
      {
        path: "/accounts/login",
        name: "Login",
        component: () => import("@/views/auth/Login.vue"),
      },
    ],
  },
  {
    path: "/store/:id",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Dashboard",
        component: () => import("@/views/dashboard/Main.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
