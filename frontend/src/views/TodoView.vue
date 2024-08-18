<template>
    <div>
        <h1>Hello World!</h1>
    </div>
</template>

<script>
import { mapStores } from 'pinia'
import { useTodoStore } from '../stores/todoStore';

    export default {
        data() {
            return {
                todoList: {}
            }
        },
        computed: {
            // note we are not passing an array, just one store after the other
            // each store will be accessible as its id + 'Store'
            ...mapStores(useTodoStore)
        },
        methods: {
        },
        async mounted () {
            try {
                await this.todoStore.fetchTodoListItems()
                this.todoList = this.todoStore.todoList
            } catch (error) {
                alert(`${error}`)
            }
        },
    }
</script>

<style lang="scss" scoped>

</style>