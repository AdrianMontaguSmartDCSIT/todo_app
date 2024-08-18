import { defineStore } from 'pinia'
import todoApiService from '../services/api.todoService'

export const useTodoStore = defineStore('todo', {
  state: () => ({
    todoList: {}
  }),
  actions: {
    async fetchTodoListItems () {
      try {
        this.items = await todoApiService.get()
      } catch (error) {
        throw error
      }
    },
    async createTodo (data) {
      try {
        const response = await todoApiService.post(data)
        this.todoList[data['category']].push(data['item'])
        console.log(response.message)
      } catch (error) {
        throw error
      }
    },
    async updateTodo (data) {
      try {
        const response = await todoApiService.put(data)
        // TODO 
        console.log(response.message)
      } catch (error) {
        throw error
      }
    },
    async deleteTodo (data) {},
    async createTodoCategory (data) {}
  }
})
