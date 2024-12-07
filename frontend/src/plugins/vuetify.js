/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

const lightMode = {
  dark: false,
  colors: {
    primary : "#335CA8",
    onPrimary : "#FFFFFF",
    primaryContainer : "#D8E2FF",
    onPrimaryContainer : "#001A42",
    secondary : "#0060AC",
    onSecondary : "#FFFFFF",
    secondaryContainer : "#D4E3FF",
    onSecondaryContainer : "#001C39",
    tertiary : "#715573",
    onTertiary : "#FFFFFF",
    tertiaryContainer : "#FCD7FB",
    onTertiaryContainer : "#2A132D",
    error : "#BA1A1A",
    errorContainer : "#FFDAD6",
    onError : "#FFFFFF",
    onErrorContainer : "#410002",
    background : "#FEFBFF", 
    onBackground : "#1B1B1F",
    surface : "#FFFBFE", // #F0F0F0
    onSurface : "#1B1B1F",
    surfaceVariant : "#E1E2EC",
    onSurfaceVariant : "#44474F",
    outline : "#75777F",
    inverseOnSurface : "#F2F0F4",
    inverseSurface : "#303034",
    inversePrimary : "#AEC6FF",
    shadow : "#000000",
    surfaceTint : "#335CA8",
    outlineVariant : "#C5C6D0",
    scrim : "#000000"
  },
}

const darkMode = {
  dark: true,
  colors: {
    primary : "#AEC6FF",
    onPrimary : "#002E6B",
    primaryContainer : "#12448F",
    onPrimaryContainer : "#D8E2FF",
    secondary : "#A4C9FF",
    onSecondary : "#00315D",
    secondaryContainer : "#004883",
    onSecondaryContainer : "#D4E3FF",
    tertiary : "#DFBBDE",
    onTertiary : "#402843",
    tertiaryContainer : "#583E5A",
    onTertiaryContainer : "#FCD7FB",
    error : "#FFB4AB",
    errorContainer : "#93000A",
    onError : "#690005",
    onErrorContainer : "#FFDAD6",
    background : "#1B1B1F",
    onBackground : "#E3E2E6",
    surface : "#1B1B1F",
    onSurface : "#E3E2E6",
    surfaceVariant : "#44474F",
    onSurfaceVariant : "#C5C6D0",
    outline : "#8E9099",
    inverseOnSurface : "#1B1B1F",
    inverseSurface : "#E3E2E6",
    inversePrimary : "#335CA8",
    shadow : "#000000",
    surfaceTint : "#AEC6FF",
    outlineVariant : "#44474F",
    scrim : "#000000"
  },
}

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    defaultTheme: 'lightMode',
    themes: {
      lightMode,
      darkMode 
    },
  } 
})
