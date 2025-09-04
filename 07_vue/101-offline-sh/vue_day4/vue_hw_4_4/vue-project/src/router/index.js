import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import UpdateView from '../views/UpdateView.vue'

const routes = [
	{
		path: '/',
		name: 'main',
		component: MainView,
	},
	{
		path: '/update/:name',
		name: 'update',
		component: UpdateView,
		props: true,
	},
]

const router = createRouter({
	history: createWebHistory(),
	routes,
})

export default router
