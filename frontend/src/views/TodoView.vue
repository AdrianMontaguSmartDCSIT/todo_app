<template>
    <div>
        {{ todoList }}
    </div>
    <div>{{ itemToAdd }}</div>
    <input type="text" v-model="itemToAdd">
    <button @click="createTodo">Add item</button>
</template>

<script>
import { mapStores } from 'pinia'
import { useTodoStore } from '../stores/todoStore';

    export default {
        data() {
            return {
                category: "",
                itemToAdd: ""
            }
        },
        computed: {
            // note we are not passing an array, just one store after the other
            // each store will be accessible as its id + 'Store'
            ...mapStores(useTodoStore),
            todoList() {
                return this.todoStore.todoList
            }
        },
        methods: {
            async addCategory() {
                const data = {
                    "category": this.category
                }
                try {
                    await this.todoStore.createTodoCategory(data)
                } catch (error) {
                    alert(error.message)
                }
            },
            async createTodo() {
                const data = {
                    "category": this.category,
                    "item": this.itemToAdd
                }
                try {
                    await this.todoStore.createTodo(data)
                    this.itemToAdd = ""
                } catch (error) {
                    alert(error)
                }
            },
            async updateTodo() {},
            async deleteTodo() {},
        },
        async mounted () {
            try {
                await this.todoStore.fetchTodoListItems()
                if (Object.keys(this.todoList).length > 0) {
                    this.category = Object.keys(this.todoList)[0]
                }
            } catch (error) {
                alert(`${error}`)
            }
        },
    }
</script>

<style lang="scss" scoped>

</style>