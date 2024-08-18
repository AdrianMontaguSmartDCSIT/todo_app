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
    createTodo () {},
    updateTodo () {},
    deleteTodo () {},
    createTodoCategory () {}
  }
})
