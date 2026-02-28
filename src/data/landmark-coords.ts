// Texas POI coordinates for itinerary geocoding.
// Keyed by lowercase normalized name. Covers top attractions across Texas destinations.
// Used by generate-itinerary.ts to resolve activity coordinates without Geocoding API calls.

export const LANDMARK_COORDS: Record<string, { lat: number; lng: number }> = {
  // ── Austin ──
  'texas state capitol': { lat: 30.2747, lng: -97.7404 },
  'south congress avenue': { lat: 30.2502, lng: -97.7498 },
  'barton springs pool': { lat: 30.2640, lng: -97.7711 },
  'zilker park': { lat: 30.2669, lng: -97.7729 },
  'lady bird lake': { lat: 30.2621, lng: -97.7514 },
  'franklin barbecue': { lat: 30.2701, lng: -97.7313 },
  'austin-bergstrom airport': { lat: 30.1975, lng: -97.6664 },
  'sixth street': { lat: 30.2672, lng: -97.7392 },
  'mount bonnell': { lat: 30.3210, lng: -97.7733 },

  // ── San Antonio ──
  'the alamo': { lat: 29.4260, lng: -98.4861 },
  'river walk': { lat: 29.4230, lng: -98.4890 },
  'san antonio missions': { lat: 29.3282, lng: -98.4545 },
  'pearl district': { lat: 29.4426, lng: -98.4812 },
  'san antonio airport': { lat: 29.5337, lng: -98.4698 },
  'mi tierra': { lat: 29.4245, lng: -98.4944 },

  // ── Houston ──
  'space center houston': { lat: 29.5519, lng: -95.0982 },
  'houston museum district': { lat: 29.7222, lng: -95.3907 },
  'george bush intercontinental airport': { lat: 29.9844, lng: -95.3414 },
  'hobby airport': { lat: 29.6454, lng: -95.2789 },
  'buffalo bayou park': { lat: 29.7628, lng: -95.3808 },
  'hermann park': { lat: 29.7134, lng: -95.3907 },

  // ── Dallas / Fort Worth ──
  'dallas arboretum': { lat: 32.8231, lng: -96.7167 },
  'dealey plaza': { lat: 32.7789, lng: -96.8083 },
  'fort worth stockyards': { lat: 32.7872, lng: -97.3476 },
  'sundance square': { lat: 32.7540, lng: -97.3309 },
  'dfw airport': { lat: 32.8968, lng: -97.0380 },
  'dallas love field': { lat: 32.8471, lng: -96.8517 },

  // ── Hill Country ──
  'enchanted rock': { lat: 30.5057, lng: -98.8198 },
  'fredericksburg main street': { lat: 30.2752, lng: -98.8720 },
  'luckenbach general store': { lat: 30.1788, lng: -98.7290 },
  'gruene hall': { lat: 29.7378, lng: -98.1054 },
  'gruene historic district': { lat: 29.7378, lng: -98.1054 },
  'wimberley square': { lat: 29.9975, lng: -98.0986 },
  'jacob\'s well': { lat: 30.0339, lng: -98.1253 },
  'hamilton pool': { lat: 30.3425, lng: -98.1269 },
  'pedernales falls': { lat: 30.3078, lng: -98.2578 },
  'comal river': { lat: 29.7100, lng: -98.1150 },
  'guadalupe river': { lat: 29.7375, lng: -98.1050 },

  // ── Big Bend / West Texas ──
  'big bend national park': { lat: 29.2500, lng: -103.2500 },
  'santa elena canyon': { lat: 29.1675, lng: -103.6089 },
  'chisos mountains': { lat: 29.2700, lng: -103.3000 },
  'marfa lights viewing area': { lat: 30.3072, lng: -103.7328 },
  'prada marfa': { lat: 30.6038, lng: -104.2186 },
  'guadalupe peak': { lat: 31.8913, lng: -104.8606 },
  'el capitan': { lat: 31.8725, lng: -104.8431 },
  'midland airport': { lat: 31.9425, lng: -102.2019 },
  'el paso airport': { lat: 31.8067, lng: -106.3781 },

  // ── Gulf Coast ──
  'galveston seawall': { lat: 29.2852, lng: -94.7961 },
  'galveston pleasure pier': { lat: 29.2853, lng: -94.7877 },
  'moody gardens': { lat: 29.2589, lng: -94.8418 },
  'south padre island beach': { lat: 26.1118, lng: -97.1681 },
  'port aransas beach': { lat: 27.8339, lng: -97.0611 },
  'padre island national seashore': { lat: 27.0492, lng: -97.3850 },
  'corpus christi bayfront': { lat: 27.7984, lng: -97.3926 },
  'uss lexington': { lat: 27.8139, lng: -97.3894 },
  'texas state aquarium': { lat: 27.8139, lng: -97.3883 },

  // ── Panhandle ──
  'palo duro canyon': { lat: 34.9414, lng: -101.7521 },
  'cadillac ranch': { lat: 35.1873, lng: -101.9872 },
  'big texan steak ranch': { lat: 35.1975, lng: -101.7927 },
  'buddy holly center': { lat: 33.5840, lng: -101.8480 },

  // ── East Texas ──
  'caddo lake': { lat: 32.7100, lng: -94.1200 },
  'jefferson general store': { lat: 32.7576, lng: -94.3499 },

  // ── Other ──
  'natural bridge caverns': { lat: 29.6925, lng: -98.3425 },
  'dinosaur valley state park': { lat: 32.2492, lng: -97.8125 },
  'fossil rim wildlife center': { lat: 32.2050, lng: -97.7950 },
};
