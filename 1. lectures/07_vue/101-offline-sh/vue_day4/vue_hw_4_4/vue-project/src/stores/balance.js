import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', {
  state: () => ({
    balances: [
      { name: '김하나', balance: 100000 },
      { name: '김두리', balance: 10000 },
      { name: '김서이', balance: 100 },
    ],
  }),
  getters: {
    getByName: (state) => (name) => {
      return state.balances.find((item) => item.name === name)
    },
  },
})
