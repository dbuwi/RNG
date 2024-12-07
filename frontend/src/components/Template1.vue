<template>
    <VContainer class="fill-height " align="center" justify="center">
      <VResponsive    >
    
        <VRow align="center" justify="center">
          <VCol style="max-width: 550px;" align="start"><h2  class="font-weight-medium text-secondary">Fullname : {{fullname}}</h2></VCol>       
        </VRow>
    
        <VRow align="center" justify="center"> 
            <VCol  style="max-width: 350px;">
              <VTextField v-model="firstname" label="First Name" wid variant="solo-inverted" clearable=""></VTextField>
              <VDivider />
              <VTextField v-model="lastname" label="Last Name" variant="solo-inverted" clearable=""></VTextField>
            </VCol>         
        </VRow>
        <VRow>
          <VCol>
            <span class="text-caption text-medium-emphasis text-error">{{ typing }}</span>
          </VCol>
        </VRow>
    
      </VResponsive>
    </VContainer>
    
    </template>
    
    <script setup>
    // IMPORTS
    import { ref,reactive,watch ,onMounted,onBeforeUnmount,computed } from "vue";  
    import { useRoute ,useRouter } from "vue-router";
    
    
    
    // VARIABLES
    const router      = useRouter();
    const route       = useRoute(); 
    const firstname   = ref("Marcus");
    const lastname    = ref("Garvey");
    const typing      = ref("");
    let timeoutVal    = 1000;
    let nameID
    
    
    // COMPUTED PROPERTIES
    const fullname = computed(()=>{    
      return `${firstname.value} ${lastname.value}`;
    });
    
    // WATCHERS
    watch(fullname,  (name) => {
      // console.log(name);  
      clearTimeout(nameID); // prevent errant multiple timeouts from being generated
      typing.value = "typing..."
      nameID = setTimeout(() => {typing.value = ""},1000);
    });
    
    // FUNCTIONS
    onMounted(()=>{
      // THIS FUNCTION IS CALLED AFTER THIS COMPONENT HAS BEEN MOUNTED
    });
    
    
    onBeforeUnmount(()=>{
      // THIS FUNCTION IS CALLED RIGHT BEFORE THIS COMPONENT IS UNMOUNTED
    });
    
    </script>
    
    <style scoped>
    /** CSS STYLE HERE */
    
    </style>
    