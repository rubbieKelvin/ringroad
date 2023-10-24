import { createRouter, createWebHistory } from "vue-router";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "",
      name: "index",
      component: () => import("@/views/index.vue"),
    },
    {
      path: "/accounts/signup",
      name: "signup",
      component: () => import("@/views/authenticate.vue"),
    },
    {
      path: "/accounts/signin",
      name: "signin",
      component: () => import("@/views/authenticate.vue"),
    },
    {
      path: "/store/create",
      name: "create-store",
      component: () => import("@/views/create-store.vue"),
    },
    {
      path: "/store/select",
      name: "select-store",
      component: () => import("@/views/select-store.vue"),
    },
    {
      path: "/store/:id",
      component: () => import("@/views/dashboard/layout.vue"),
      children: [
        {
          path: "/",
          name: "dashboard-home",
          component: () => import("@/views/dashboard/index.vue"),
        },
      ],
    },
  ],
});
