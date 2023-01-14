import { defineStore } from 'pinia'

export const useTaskListStore = defineStore('taskList', {
  state: () => ({ taskList: [] }),
  getters: {
    task: state => state.taskList,
  },
  actions: {
    addTask(input) {
      this.taskList.push({ task: input, status: 0 })
    },
    taskIs(id, nbr) {
      this.taskList[id].status = nbr;
    },
    taskEdit(id, task) {
      this.taskList[id].task = task;
    },
    taskDeleted(id) {
      this.taskList.splice(id, 1);
    }
  },
})
