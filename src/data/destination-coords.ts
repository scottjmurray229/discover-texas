// Shared destination coordinates — single source of truth
// Used by plan page + companion app + generate-itinerary API.

export const DESTINATION_COORDS: Record<string, { lat: number; lng: number; label: string }> = {
  // Central Texas
  austin: { lat: 30.2672, lng: -97.7431, label: 'Austin' },
  'san-antonio': { lat: 29.4241, lng: -98.4936, label: 'San Antonio' },
  waco: { lat: 31.5493, lng: -97.1467, label: 'Waco' },
  georgetown: { lat: 30.6333, lng: -97.6780, label: 'Georgetown' },
  'round-rock': { lat: 30.5083, lng: -97.6789, label: 'Round Rock' },
  'new-braunfels': { lat: 29.7030, lng: -98.1245, label: 'New Braunfels' },
  'san-marcos': { lat: 29.8833, lng: -97.9414, label: 'San Marcos' },
  killeen: { lat: 31.1171, lng: -97.7278, label: 'Killeen' },
  'temple-belton': { lat: 31.0982, lng: -97.3428, label: 'Temple-Belton' },
  'bryan-college-station': { lat: 30.6744, lng: -96.3698, label: 'Bryan-College Station' },

  // Gulf Coast
  houston: { lat: 29.7604, lng: -95.3698, label: 'Houston' },
  galveston: { lat: 29.3013, lng: -94.7977, label: 'Galveston' },
  'corpus-christi': { lat: 27.8006, lng: -97.3964, label: 'Corpus Christi' },
  'south-padre-island': { lat: 26.1118, lng: -97.1681, label: 'South Padre Island' },
  'port-aransas': { lat: 27.8339, lng: -97.0611, label: 'Port Aransas' },
  'port-isabel': { lat: 26.0715, lng: -97.2086, label: 'Port Isabel' },
  'rockport-fulton': { lat: 28.0206, lng: -97.0544, label: 'Rockport-Fulton' },
  matagorda: { lat: 28.6869, lng: -95.9677, label: 'Matagorda' },
  'surfside-beach': { lat: 28.9467, lng: -95.2919, label: 'Surfside Beach' },

  // Hill Country
  fredericksburg: { lat: 30.2752, lng: -98.8720, label: 'Fredericksburg' },
  wimberley: { lat: 29.9975, lng: -98.0986, label: 'Wimberley' },
  'dripping-springs': { lat: 30.1902, lng: -98.0867, label: 'Dripping Springs' },
  bandera: { lat: 29.7266, lng: -99.0736, label: 'Bandera' },
  boerne: { lat: 29.7947, lng: -98.7320, label: 'Boerne' },
  kerrville: { lat: 30.0474, lng: -99.1404, label: 'Kerrville' },
  'johnson-city': { lat: 30.2769, lng: -98.4120, label: 'Johnson City' },
  luckenbach: { lat: 30.1788, lng: -98.7290, label: 'Luckenbach' },
  'marble-falls': { lat: 30.5782, lng: -98.2750, label: 'Marble Falls' },
  'enchanted-rock': { lat: 30.5057, lng: -98.8198, label: 'Enchanted Rock' },

  // West Texas
  'big-bend': { lat: 29.2500, lng: -103.2500, label: 'Big Bend' },
  marfa: { lat: 30.3087, lng: -104.0213, label: 'Marfa' },
  'el-paso': { lat: 31.7619, lng: -106.4850, label: 'El Paso' },
  alpine: { lat: 30.3585, lng: -103.6610, label: 'Alpine' },
  terlingua: { lat: 29.3225, lng: -103.6102, label: 'Terlingua' },
  'guadalupe-mountains': { lat: 31.8913, lng: -104.8606, label: 'Guadalupe Mountains' },
  abilene: { lat: 32.4487, lng: -99.7331, label: 'Abilene' },
  'midland-odessa': { lat: 31.9973, lng: -102.0779, label: 'Midland-Odessa' },

  // North Texas
  dallas: { lat: 32.7767, lng: -96.7970, label: 'Dallas' },
  'fort-worth': { lat: 32.7555, lng: -97.3308, label: 'Fort Worth' },
  denton: { lat: 33.2148, lng: -97.1331, label: 'Denton' },
  grapevine: { lat: 32.9343, lng: -97.0781, label: 'Grapevine' },
  mckinney: { lat: 33.1972, lng: -96.6397, label: 'McKinney' },
  granbury: { lat: 32.4419, lng: -97.7942, label: 'Granbury' },
  'glen-rose': { lat: 32.2346, lng: -97.7553, label: 'Glen Rose' },

  // East Texas
  jefferson: { lat: 32.7576, lng: -94.3499, label: 'Jefferson' },
  'caddo-lake': { lat: 32.7100, lng: -94.1200, label: 'Caddo Lake' },

  // South Texas
  brownsville: { lat: 25.9017, lng: -97.4975, label: 'Brownsville' },
  laredo: { lat: 27.5036, lng: -99.5076, label: 'Laredo' },
  mcallen: { lat: 26.2034, lng: -98.2300, label: 'McAllen' },
  'del-rio': { lat: 29.3627, lng: -100.8968, label: 'Del Rio' },
  'eagle-pass': { lat: 28.7091, lng: -100.4995, label: 'Eagle Pass' },
  kingsville: { lat: 27.5159, lng: -97.8561, label: 'Kingsville' },

  // Panhandle
  amarillo: { lat: 35.2220, lng: -101.8313, label: 'Amarillo' },
  lubbock: { lat: 33.5779, lng: -101.8552, label: 'Lubbock' },
  canyon: { lat: 34.9803, lng: -101.9188, label: 'Canyon' },
  'palo-duro-canyon': { lat: 34.9414, lng: -101.7521, label: 'Palo Duro Canyon' },

  // Piney Woods
  tyler: { lat: 32.3513, lng: -95.3011, label: 'Tyler' },
  nacogdoches: { lat: 31.6035, lng: -94.6555, label: 'Nacogdoches' },
  lufkin: { lat: 31.3382, lng: -94.7291, label: 'Lufkin' },
};
