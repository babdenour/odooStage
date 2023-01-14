// import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createPinia } from 'pinia'


// createApp(App).use(createPinia()).mount('#app')



import { createApp, provide, h } from 'vue'
import { DefaultApolloClient } from '@vue/apollo-composable'

import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'

// HTTP connection to the API
const httpLink = createHttpLink({
  // You should use an absolute URL here
  uri: 'http://localhost:8000/graphql',
})

// Cache implementation
const cache = new InMemoryCache()

// Create the apollo client
const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
})



const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient, createPinia())
  },

  render: () => h(App),
})

app.mount('#app')
