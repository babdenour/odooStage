<template>
  <div class="w-full px-2 py-16 sm:px-0">
    <TabGroup>
      <TabList class="flex w-full flex-row space-x-5 rounded-xl p-1">
        <ListBulletIcon class="w-36 text-gray-400 m-1" />
        <h1 class="text-gray-400 flex ">
          To Do List
        </h1>
        <Tab v-for="category in categories" as="template" :key="category" v-slot="{ selected }">
          <button :class="[
            'w-full rounded-lg py-2.5 text-sm font-medium leading-5 text-gray-400',
            selected
              ? 'bg-gray-800 shadow-md'
              : 'text-gray-400',
          ]">
            {{ category }}
          </button>
        </Tab>
      </TabList>
      <div>
        <input class="bg-gray-800/[0.1] rounded-md p-3 m-3 shadow-md focus:outline-none text-gray-400"
          placeholder="Add new task" v-model="input" @keyup.enter="save(input)" />
        <button v-if="editTask" type="submit" class="bg-gray-800 text-gray-400 rounded-md p-3 m-3"
          @click="edit(input)">EDIT</button>
        <button v-if="!editTask" type="submit" class="bg-gray-800 text-gray-400 rounded-md p-3 m-3"
          @click="save(input)">ADD</button>
      </div>
      <TabPanels class="mt-2">
        <TabPanel :class="[
          'rounded-xl bg-gray-700 p-3 focus:outline-none ',
        ]">
          <ul>
            <li v-for="(task, idx) of taskList" :key="idx" @click="toggle(idx)" :class="['flex place-content-between w-full rounded-r-md p-3 m-3 text-gray-400 bg-gray-800 hover:cursor-pointer border-l-4',
          taskList[idx].status === 1
            ? 'border-green-500'
            : 'border-red-500']">
              <p class="text-sm font-medium leading-5 ">
                {{ task.task }}
              </p>
              <div class="flex">
                <TrashIcon class="w-5 text-red-500 m-1" @click.stop="tStore.taskDeleted(idx)" />
                <PencilSquareIcon class="w-5 text-green-500 m-1" @click.stop="test" />
              </div>
            </li>
          </ul>
        </TabPanel>
        <TabPanel :class="[
          'rounded-xl bg-gray-700 p-3 focus:outline-none ',
        ]">
          <ul>
            <li v-for="(task, idx) of taskList.filter(e => e.status === 1)" :key="idx" @click="toggle(idx)"
              class="flex place-content-between w-full rounded-r-md p-3 m-3 text-gray-400 bg-gray-800 hover:cursor-pointer border-l-4 border-green-500">
              <p class="text-sm font-medium leading-5 ">
                {{ task.task }}
              </p>
              <div class="flex">
                <TrashIcon class="w-5 text-red-500 m-1" @click.stop="tStore.taskDeleted(idx)" />
                <PencilSquareIcon class="w-5 text-green-500 m-1" @click.stop="test" />
              </div>
            </li>
          </ul>
        </TabPanel>
        <TabPanel :class="[
          'rounded-xl bg-gray-700 p-3 focus:outline-none ',
        ]">
          <ul>
            <li v-for="(task, idx) of taskList.filter(e => e.status === 0)" :key="idx" @click="toggle(idx)"
              class="flex place-content-between w-full rounded-r-md p-3 m-3 text-gray-400 bg-gray-800 hover:cursor-pointer border-l-4 border-red-500">
              <p class="text-sm font-medium leading-5 ">
                {{ task.task }}
              </p>
              <div class="flex">
                <TrashIcon class="w-5 text-red-500 m-1" @click.stop="tStore.taskDeleted(idx)" />
                <PencilSquareIcon class="w-5 text-green-500 m-1" @click.stop="test" />
              </div>
            </li>
          </ul>
        </TabPanel>
      </TabPanels>

    </TabGroup>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { TabGroup, TabList, Tab, TabPanels, TabPanel } from "@headlessui/vue";
import { useTaskListStore } from '../store/index.js'
import { PencilSquareIcon, TrashIcon, ListBulletIcon } from '@heroicons/vue/24/solid'

const tStore = useTaskListStore()
const categories = ref(['All', 'Done', 'Undone']);

const taskList = tStore.task;
const editTask = ref(false);
const input = ref('');

const edit = (id, name) => {
  tStore.taskEdit(id, name)
  editTask.value = '';
}

const save = (task) => {
  input.value = '';
  tStore.addTask(task);
}

const toggle = (id) => {
  let nbr;
  taskList[id].status === 0 ? nbr = 1 : nbr = 0;
  tStore.taskIs(id, nbr);
}
</script>
