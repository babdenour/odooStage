<template>
  <ul>
    <li style="color: white" v-for="res in result" :key="idx">
      {{ res[0].author }} <br /> {{ res[0].title }} </li>
  </ul>
</template>

<script setup>
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'

const { result } = useQuery(gql`
      query getUsers {
        books {
          author
          title
        }
      }
    `)
</script>

rzu@open-net.ch
dga@open-net.ch