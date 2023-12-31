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
      path: "/auth/callback",
      name: "auth-callback",
      component: () => import("@/views/authenticate.vue"),
    },
    {
      path: "/store/create",
      name: "create-store",
      component: () => import("@/views/create-store.vue"),
    },
    {
      path: "/store/:id",
      component: () => import("@/views/dashboard/layout.vue"),
      children: [
        {
          path: "",
          name: "dashboard-home",
          component: () => import("@/views/dashboard/index.vue"),
        },
        {
          path: "inventory",
          name: "dashboard-products",
          component: () => import("@/views/dashboard/products.vue"),
        },
        {
          path: "customers",
          name: "dashboard-customers",
          component: () => import("@/views/dashboard/customers.vue"),
        },
        {
          path: "transactions",
          name: "dashboard-transactions",
          component: () => import("@/views/dashboard/transactions.vue"),
        },
      ],
    },
  ],
});
