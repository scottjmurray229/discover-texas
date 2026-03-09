import type { PackingItem, PackingConfig, GearRecommendation } from './packing-base';

export const TEXAS_ESSENTIALS: PackingItem[] = [
  { id: 'tx-sun', name: 'Sun Protection (SPF 50 + hat)', category: 'destination', description: 'Texas summer UV is brutal — West Texas and the Hill Country hit UV index 10+ daily from May–September. A wide-brim hat and SPF 50 sunscreen are the two most important items.', essential: true, amazonSearchFallback: 'wide+brim+hat+sun+protection+upf', affiliatePrice: '$25–45' },
  { id: 'tx-boots', name: 'Cowboy Boots / Walking Boots', category: 'destination', description: 'In Texas, boots are not a costume — they\'re functional footwear for everything from honky-tonks to Big Bend hiking. Even a basic pair elevates the experience and fits right in.', essential: false, amazonSearchFallback: 'cowboy+boots+western+leather+travel', affiliatePrice: '$80–200', localAlternative: 'Buy at any Boot Barn or Cavender\'s — better selection in Texas than online anyway' },
  { id: 'tx-layers', name: 'Layers for AC Culture', category: 'destination', description: 'Texas air conditioning is set to arctic temperatures in summer — restaurants, museums, and offices keep it at 65°F when it\'s 100°F outside. Always carry a layer.', essential: true, amazonSearchFallback: 'packable+lightweight+cardigan+layer', affiliatePrice: '$20–40' },
  { id: 'tx-water', name: 'Large Reusable Water Bottle', category: 'destination', description: 'Texas heat requires constant hydration. Big Bend National Park has water sources miles apart. Even Austin and San Antonio require more water than you think in summer heat.', essential: true, amazonSearchFallback: 'insulated+water+bottle+32oz+64oz', affiliatePrice: '$20–35' },
];

export const TEXAS_GEAR_RECOMMENDATIONS: GearRecommendation[] = [
  { id: 'gr-tx-hat', name: 'Wide-Brim Sun Hat', reason: 'Texas summer sun is relentless from the Panhandle to the Gulf. A wide-brim hat in the Hill Country, Big Bend, or South Padre Island is the difference between enjoying the day and retreating inside.', amazonSearchFallback: 'wide+brim+sun+hat+upf+outdoor', affiliatePrice: '~$35' },
  { id: 'gr-tx-water', name: 'Insulated Water Bottle (64oz)', reason: 'Big Bend temperatures hit 120°F in summer. Even Houston and Austin require 3+ liters/day of hydration. An insulated bottle keeps water cold for hours when you need it most.', amazonSearchFallback: 'insulated+water+bottle+64oz+stainless', affiliatePrice: '~$35' },
  { id: 'gr-tx-sunscreen', name: 'SPF 50+ Sunscreen', reason: 'Texas UV index regularly hits 10–11 from May through September. Even cloud cover doesn\'t block UV. Apply before going out and reapply every 90 minutes near water or outdoors.', amazonSearchFallback: 'sunscreen+spf+50+sport+water+resistant', affiliatePrice: '~$15' },
  { id: 'gr-tx-boots', name: 'Cowboy Boots', reason: 'You\'re in Texas — and boots are practical here, not costume. From Houston dance floors to Big Bend trails to Austin\'s Sixth Street, boots belong on Texas feet. Buy at Cavender\'s on arrival.', amazonSearchFallback: 'cowboy+boots+leather+western+comfortable', affiliatePrice: '~$150' },
  { id: 'gr-tx-layer', name: 'Packable Cardigan / Light Jacket', reason: 'Texas AC is set to 65°F when it\'s 100°F outside. Every restaurant, museum, and office is frigid in summer. A packable layer means you\'re not shivering through dinner after sweating through the afternoon.', amazonSearchFallback: 'packable+cardigan+lightweight+layer+travel', affiliatePrice: '~$25' },
];

export const TEXAS_CONFIG: PackingConfig = {
  sitePrefix: 'dtx',
  destination: 'Texas',
  climate: ['desert', 'temperate'],
  currency: 'USD',
  plugType: 'Type A/B',
  plugVoltage: '120V',
  affiliateTag: 'discoverphili-20',
  destinationEssentials: TEXAS_ESSENTIALS,
  gearRecommendations: TEXAS_GEAR_RECOMMENDATIONS,
};

export const SITE_CONFIG = TEXAS_CONFIG;

export const TEXAS_PACKING_FAQS = [
  { question: 'What should I pack for Texas?', answer: 'The Texas essentials: SPF 50 sunscreen and a wide-brim hat (UV index hits 11+ in summer), a large water bottle (constant hydration required), light layers for aggressive AC culture, and comfortable walking boots. Texas is large and varied — Big Bend needs hiking gear, while Austin and Houston call for city casual.' },
  { question: 'How hot does Texas get?', answer: 'Texas summer is serious. West Texas and the Hill Country regularly hit 105°F from June–August. Big Bend averages 115°F in July. Coastal Texas (Corpus Christi, South Padre) adds high humidity. Spring (March–May) and fall (October–November) are the ideal times to visit outdoor Texas.' },
  { question: 'What power adapter do I need for Texas?', answer: 'No adapter needed — Texas uses standard US Type A/B plugs at 120V/60Hz. Everything works as-is.' },
  { question: 'What should I wear in Texas?', answer: 'Casual and practical. In summer: lightweight breathable fabrics, covered shoulders for sun protection (UPF shirts are better than sunscreen alone), and comfortable walking shoes or boots. For Austin nightlife: smart casual. For cowboy country (Fort Worth, Amarillo): boots and western wear are genuinely appropriate and locally respected.' },
  { question: 'Do I need hiking gear for Big Bend National Park?', answer: 'Yes — Big Bend is serious desert hiking. Minimum kit: 3–4 liters of water per person per day (more in summer), waterproof hiking boots, UPF sun shirt, wide-brim hat, SPF 50 sunscreen, and electrolyte packets. Summer hiking in Big Bend (June–August) should be restricted to early morning before 10am.' },
  { question: 'What should I NOT bring to Texas?', answer: 'Skip heavy clothing (Texas heat makes most winter gear useless from April–October), flip-flops for outdoor hiking (wrong footwear for rocky Texas terrain), and any assumption that one Texas city is like another — Houston is subtropical humidity, El Paso is dry desert, Austin is Hill Country — they pack differently.' },
];
