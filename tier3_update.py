#!/usr/bin/env python3
"""Texas Tier 3 quality pass — upgrades all 59 destination files with affiliatePicks, faqItems, scottTips, immersive-break-inline, AEO ledes"""
import os

BASE = "C:/Users/scott/Documents/discover-texas/src/content/destinations"

BOOKING = "https://www.booking.com/region/us/texas.html?aid=2778866"
GYG = "https://www.getyourguide.com/?partner_id=IVN6IQ3"
AMAZON = "https://www.amazon.com/s?k=texas+travel&tag=discovermore-20"

# Full detailed data for priority destinations
PRIORITY = {
    "austin": {
        "description": "Austin is Texas's state capital and cultural heart — the Live Music Capital of the World with 250+ live music venues, Franklin Barbecue, Sixth Street, Lady Bird Lake kayaking, and a tech industry boom that's made it one of America's fastest-growing cities.",
        "tagline": "Live Music Capital of the World",
        "region": "central-texas",
        "aeo": "Austin is Texas's state capital and the self-proclaimed Live Music Capital of the World — a rapidly growing city of 1 million people with 250+ live music venues, some of the best barbecue in the state (Franklin Barbecue), the Congress Avenue bridge bat colony, Lady Bird Lake outdoor recreation, and a 'Keep Austin Weird' counterculture that's increasingly under pressure from tech industry growth.",
        "gradient": "linear-gradient(135deg, #1e40af, #7c3aed, #166534)",
        "video_title": "Austin: Keep It Weird",
        "video_text": "Live music, Franklin BBQ, bats, and Lady Bird Lake.",
        "faqItems": [
            {"q": "Is Franklin Barbecue worth the wait?", "a": "Yes, if you can get there. Franklin Barbecue is widely considered the best BBQ in Texas (which makes it arguably the best in the world). The line forms by 8am for an 11am opening; show up by 8:30 to be safe. Brisket and the beef rib are the essential orders. Cash only. Plan your morning around it."},
            {"q": "What is South by Southwest (SXSW)?", "a": "SXSW is the massive annual music, film, and tech conference held in Austin for 10 days in mid-March. Over 400,000 attendees fill the city. Hotels book solid 12+ months out at premium prices. If you want to attend, plan a year ahead. If you don't want SXSW crowds, avoid Austin in March."},
            {"q": "When is the best time to visit Austin?", "a": "October–November and March–April (avoiding SXSW week). Summers are brutal — 100°F+ for weeks at a time. The shoulder seasons have music festivals and comfortable weather. ACL Music Festival (October) is a better time to experience Austin's music identity than navigating SXSW."},
            {"q": "What is the bat colony under Congress Avenue Bridge?", "a": "From March through October, 1.5 million Mexican free-tailed bats live under the Congress Avenue Bridge over Lady Bird Lake. At sunset, they emerge for their nightly insect hunt in a column that can take 45 minutes to fully emerge. Free to watch from the bridge or the lawn below. One of the most remarkable urban wildlife experiences in the US."},
            {"q": "What is 6th Street?", "a": "6th Street is Austin's main live music corridor — a stretch of bars and venues that becomes a pedestrian zone on weekend nights. The eastern section (East 6th) has more indie bars; the western section (Dirty 6th) is louder and more tourist-oriented. For the best live music experience, try Red River Cultural District (parallel, one block north) or the Continental Club on South Congress."},
            {"q": "What is the best live music venue in Austin?", "a": "Continental Club (classic Texas country and blues, 1957). Stubb's Amphitheatre (outdoor, 2,000 capacity, major acts). Emo's (the indie/punk venue). For country, the Broken Spoke is the authentic two-step dance hall experience. Sixth Street has dozens of free-entry options for wandering."},
            {"q": "Is Austin expensive?", "a": "Increasingly yes — Austin's tech boom has significantly raised accommodation and restaurant prices. Hotels near downtown run $180–300/night. Budget travelers can use the university area (UT) hostels. Food ranges from $10 food trucks to $80+ fine dining. The live music venues often have free or cheap cover charges."},
            {"q": "Do I need a car in Austin?", "a": "Car helpful but not essential for central Austin. Uber/Lyft are reliable and affordable. The 6th Street area and South Congress are walkable. Capital Metro light rail (MetroRail) connects downtown to the Domain (tech corridor). Rent a car for day trips to Fredericksburg, Enchanted Rock, or San Antonio."},
        ],
        "affiliatePicks": [
            {"name": "Hotel Saint Cecilia Austin", "type": "hotel", "url": "https://www.booking.com/hotel/us/saint-cecilia-austin.html?aid=2778866", "description": "South Congress boutique hotel named after the patron saint of musicians. Rock-star aesthetic, private pool.", "priceRange": "$$$$"},
            {"name": "Franklin Barbecue Reservation", "type": "restaurant", "url": "https://www.getyourguide.com/austin-l191/?partner_id=IVN6IQ3&q=Franklin+BBQ+Austin", "description": "Franklin offers limited online reservations — check before planning your line strategy.", "priceRange": "$$"},
            {"name": "Austin Bat Colony and City Kayak Tour", "type": "tour", "url": "https://www.getyourguide.com/austin-l191/?partner_id=IVN6IQ3&q=Austin+kayak+bat+tour", "description": "Kayak tour on Lady Bird Lake with bat colony viewing at sunset.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Austin-Bergstrom International (AUS) is 8 miles southeast — 20-minute Lyft to downtown. SXSW (mid-March) and ACL Fest (October weekend) cause hotel price spikes — book months ahead or avoid. San Antonio is 1.5 hours south; excellent day trip pairing.",
            "bestTime": "October–November for ACL Fest, cooler weather, and Austin at its most enjoyable. March–April (avoiding SXSW). Avoid June–August unless you have access to a pool and air conditioning.",
            "gettingAround": "Lyft/Uber for most of the city. Walk 6th Street and South Congress. Rent a car for day trips to the Hill Country (Fredericksburg, Marble Falls, Wimberley).",
            "money": "Austin's tech boom has made it expensive. Budget $180–300/night for decent downtown hotels. Live music venues often have $5-$15 cover or none. Franklin BBQ is $28–$35/lb depending on the cut.",
            "safety": "Downtown and tourist areas are safe. 6th Street late night (after midnight) gets rowdy — standard awareness.",
            "packing": "Light clothes for the heat. Good walking shoes for 6th Street. Earplugs if you're a light sleeper near any live music venue.",
            "localCulture": "Austin has a strong 'Keep Austin Weird' identity under pressure from rapid growth. The city's liberal politics are distinct within Texas. Tipping culture is strong — the service industry is underpaid. The breakfast taco is Austin's sacred morning ritual and the subject of neighborhood debates."
        },
    },
    "san-antonio": {
        "description": "San Antonio is Texas's most visited city — a rich blend of Spanish colonial heritage, the Alamo, the River Walk, and the best Mexican food in Texas.",
        "tagline": "Where history meets the river",
        "region": "south-texas",
        "aeo": "San Antonio is Texas's most visited city and one of the oldest in North America — a Spanish colonial city with the Alamo (the most visited landmark in Texas), the River Walk (a limestone-lined urban river with restaurants and bars 20 feet below street level), and an authentic Mexican-American culture that produces the best Tex-Mex food in the state. It's 1.5 hours from Austin and an excellent pairing.",
        "gradient": "linear-gradient(135deg, #dc2626, #92400e, #166534)",
        "video_title": "San Antonio: The River City",
        "video_text": "The Alamo, the River Walk, and the best Tex-Mex in Texas.",
        "faqItems": [
            {"q": "Is the Alamo worth visiting?", "a": "Yes — the Alamo is genuinely moving as a historical site, regardless of how you feel about the Texas mythology that surrounds it. The main shrine (the original chapel) is small; the surrounding grounds and museum provide the context. Free admission. Arrive early to avoid lines — 9am opens with far smaller crowds than midday."},
            {"q": "What is the River Walk?", "a": "The River Walk (Paseo del Rio) is a limestone-paved pedestrian path 20 feet below street level, running 15 miles along the San Antonio River through downtown. The tourist-heavy main loop has restaurant patios, bars, hotels, and boat tours. Explore the Museum Reach (north) and Mission Reach (south) for the less touristy, more beautiful sections."},
            {"q": "What is the best Tex-Mex in San Antonio?", "a": "Mi Tierra Cafe (open 24 hours, colorful, historic) for enchiladas. Rosario's for fajitas and a margarita. Güero's (the Austin favorite) is actually an Austin institution — SA equivalents are better. La Fonda on Main for a quieter, more refined Tex-Mex experience. The Mexican-American community in San Antonio produces food that's authentically derived from Nuevo León cuisine rather than Americanized."},
            {"q": "What are the San Antonio Missions?", "a": "San Antonio Missions National Historical Park preserves four Spanish colonial missions (Mission Concepción, Mission San José, Mission San Juan, and Mission Espada) that were active communities in the 1700s. Together with the Alamo, they form a UNESCO World Heritage Site. All are on the Mission Trail bike and pedestrian path. Mission San José is the most impressive — the ornate Baroque facade is extraordinary."},
            {"q": "When is the best time to visit San Antonio?", "a": "March–May and October–November. San Antonio averages warmer temperatures than Austin — summer (May–September) is very hot (95°F+). Fiesta San Antonio (April, 10 days) is the city's largest celebration — hundreds of events, parades, and parties."},
            {"q": "How do I get between San Antonio and Austin?", "a": "I-35 connects the two cities — 80 miles, normally 1.5 hours but traffic in Austin can extend it significantly. Greyhound and FlixBus offer bus service. No Amtrak. Shuttles exist but are infrequent."},
            {"q": "What is the Pearl District?", "a": "The Pearl District is a former brewery complex on the Museum Reach of the River Walk, transformed into San Antonio's best dining and entertainment destination. Hotel Emma is the landmark hotel. The Saturday farmers market is excellent. The restaurant cluster includes hot.chicken, Cured, and Southerleigh Fine Food & Brewery."},
            {"q": "Is San Antonio a good city for families?", "a": "Excellent. Sea World San Antonio and Six Flags Fiesta Texas are nearby. The missions are educational. The River Walk is walkable and safe. The San Antonio Zoo in Brackenridge Park is well-regarded."},
        ],
        "affiliatePicks": [
            {"name": "Hotel Emma at the Pearl", "type": "hotel", "url": "https://www.booking.com/hotel/us/emma-san-antonio.html?aid=2778866", "description": "The finest hotel in San Antonio — in the historic Pearl Brewery with extraordinary design and River Walk access.", "priceRange": "$$$$"},
            {"name": "San Antonio River Walk Boat Tour", "type": "tour", "url": "https://www.getyourguide.com/san-antonio-l192/?partner_id=IVN6IQ3&q=River+Walk+boat+tour", "description": "Narrated boat tour of the River Walk — the best introduction to downtown San Antonio.", "priceRange": "$"},
            {"name": "Alamo and Missions Walking Tour", "type": "tour", "url": "https://www.getyourguide.com/san-antonio-l192/?partner_id=IVN6IQ3&q=Alamo+Missions+tour", "description": "Guided tour of the Alamo and San Antonio Missions UNESCO World Heritage sites.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "San Antonio International Airport (SAT) is 8 miles north of downtown. VIA bus service runs to downtown. Lyft/Uber are more practical. The River Walk hotel cluster puts you within walking distance of most tourist sites.",
            "bestTime": "March–May for pleasant weather. April brings Fiesta San Antonio. November–February is mild and less crowded. Avoid July–August peak heat.",
            "gettingAround": "River Walk is walkable for the tourist core. VIA bus system covers the city. Rent a car for the Mission Trail (4 missions south of downtown) and Hill Country day trips.",
            "money": "San Antonio is more affordable than Austin. Hotels on the River Walk run $150–250/night; a few blocks away cuts to $100–150. Tex-Mex meals at local spots run $12–25/person.",
            "safety": "River Walk and downtown are safe tourist zones. San Antonio has a large military population (5 bases) that contributes to a structured civic culture.",
            "packing": "Light clothing for the heat. Walking shoes for the River Walk's stone paths and the Mission Trail. Sun protection.",
            "localCulture": "San Antonio is the most Mexican-American major city in the US (with a deeper historical roots than most cities' Latino communities — many families have been here since Spanish colonial times). The food here is genuine, not Americanized. The margarita is taken seriously."
        },
    },
    "houston": {
        "description": "Houston is the 4th largest US city — an international energy capital with the best food scene in Texas, NASA's Johnson Space Center, and a world-class Museum District.",
        "tagline": "Space City, energy capital, food paradise",
        "region": "gulf-coast",
        "aeo": "Houston is the 4th largest city in the United States — a massive, sprawling energy capital on the Gulf Coast with the most diverse and arguably best restaurant scene in Texas, NASA's Johnson Space Center, the largest medical complex in the world (Texas Medical Center), and a Museum District with 19 cultural institutions. It has no zoning laws, which produces a chaotic but creative urban landscape.",
        "gradient": "linear-gradient(135deg, #1e40af, #dc2626, #f59e0b)",
        "video_title": "Houston: Space City",
        "video_text": "NASA, the world's best restaurant diversity, and 2 million acres of no zoning.",
        "faqItems": [
            {"q": "What is unique about Houston's food scene?", "a": "Houston's lack of zoning laws and its position as the most ethnically diverse large city in the US has produced an extraordinary food landscape. The city has the largest Vietnamese population outside of Vietnam in one area (Beltway 8 corridor), excellent Nigerian and Ethiopian food, outstanding Tex-Mex, and James Beard Award-winning fine dining. The food trucks are serious, the dim sum is excellent, and the crawfish is freshwater-boiled Cajun style."},
            {"q": "Is NASA Johnson Space Center worth visiting?", "a": "Yes — Space Center Houston (the visitor center at Johnson Space Center, 25 miles south of downtown) is excellent. Tram tours take you through the historic Mission Control (where 'Houston, we have a problem' was actually spoken) and the ISS training facility. Budget half a day minimum."},
            {"q": "What neighborhoods should I explore in Houston?", "a": "Montrose for the arts and LGBTQ+ scene, independent restaurants, and galleries. The Heights for the Victorian neighborhood feel and coffee shops. Midtown for nightlife. The Museum District for culture. The Galleria area for upscale shopping (and not much else). Avoid driving downtown — parking is a nightmare."},
            {"q": "What is Houston's museum scene?", "a": "The Museum District has 19 institutions within walking distance — the Museum of Fine Arts Houston (world-class, admission required), the Houston Museum of Natural Science (free Thursdays), the Holocaust Museum, the Menil Collection (free, one of the finest art museums in the US), and the Rothko Chapel (free, spiritual)."},
            {"q": "When is the best time to visit Houston?", "a": "October–April. Houston's heat and humidity from May through September are oppressive — 95°F+ with 90% humidity. The Houston Livestock Show and Rodeo (February–March) is the largest annual attended event in the US. October–December is the best weather window."},
            {"q": "How do I get around Houston?", "a": "Car is essential — Houston is one of the most car-dependent cities in the US. The METROrail light rail runs through the Museum District and Medical Center to downtown but covers limited ground. Budget for parking or use Lyft/Uber extensively."},
            {"q": "What is the best BBQ in Houston?", "a": "Killen's BBQ in Pearland (45 minutes south) is the Houston area benchmark — wagyu brisket and beef ribs that rival Central Texas BBQ. Gatlin's BBQ in the Heights is excellent and easier to access. Truth BBQ in the Heights (from Brenham) is a newer entrant with a strong following."},
            {"q": "Is Houston worth visiting for a short trip?", "a": "Yes — 2–3 days covers the Museum District (Menil Collection and one other museum), Space Center Houston, one excellent Montrose/Heights restaurant day, and a Vietnamese dinner on the Beltway 8 corridor. Houston rewards visitors who engage with its food diversity specifically."},
        ],
        "affiliatePicks": [
            {"name": "Hotel Granduca Houston", "type": "hotel", "url": "https://www.booking.com/hotel/us/hotel-granduca.html?aid=2778866", "description": "Italian villa-inspired luxury hotel in the Galleria area — Houston's most elegant hotel option.", "priceRange": "$$$$"},
            {"name": "Space Center Houston Admission", "type": "activity", "url": "https://www.getyourguide.com/houston-l190/?partner_id=IVN6IQ3&q=NASA+Space+Center+Houston", "description": "Advance tickets for Space Center Houston including tram tour of Mission Control.", "priceRange": "$$"},
            {"name": "Houston Food Tour — Montrose and Heights", "type": "tour", "url": "https://www.getyourguide.com/houston-l190/?partner_id=IVN6IQ3&q=Houston+food+tour", "description": "Guided food tour through Houston's most diverse and interesting dining neighborhoods.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Two airports: George Bush Intercontinental (IAH, United hub, 23 miles north) and Hobby (HOU, Southwest hub, 10 miles southeast). IAH is the main international gateway. Fly between Houston and other Texas cities rather than driving — distances are extreme.",
            "bestTime": "October–April. The Houston Livestock Show and Rodeo (February–March) is worth seeing. Summer heat and humidity are severe.",
            "gettingAround": "Car essential. METROrail is useful for Museum District and Medical Center. Parking is free at most Houston attractions and malls — the sprawl is designed for cars.",
            "money": "Houston is more affordable than expected for its size. Hotels in the Galleria area run $130–200/night. Museum District is walkable once you're there. The Menil Collection is free.",
            "safety": "Montrose, the Heights, and the Museum District are safe tourist areas. Downtown Houston has some areas to avoid after dark. Standard urban awareness.",
            "packing": "Light clothing for the heat. Umbrella — afternoon thunderstorms are common. Car for everything.",
            "localCulture": "Houston's no-zoning law is the key to understanding the city — it's the only major US city without traditional zoning, which produces strange adjacencies (strip mall next to Victorian house next to glass office tower). The city's identity is shaped by the oil industry, NASA, and the port. Houstonians are proud of the diversity and the food scene."
        },
    },
    "dallas": {
        "description": "Dallas is Texas's business capital — a glass-and-steel skyline city with the Sixth Floor Museum at Dealey Plaza, Deep Ellum's music scene, world-class arts institutions, and excellent Tex-Mex.",
        "tagline": "Big D, where business meets culture",
        "region": "north-texas",
        "aeo": "Dallas is Texas's financial and business capital — a gleaming skyline city of 1.3 million (metro area 7+ million) that's home to the Sixth Floor Museum at Dealey Plaza (JFK assassination site), the Dallas Museum of Art, Deep Ellum's music and bar scene, and some of the best Indian food in the South. It's 30 minutes from Fort Worth, which has a legitimate Western heritage.",
        "gradient": "linear-gradient(135deg, #1e40af, #dc2626, #166534)",
        "video_title": "Dallas: Big D",
        "video_text": "JFK, Deep Ellum, and a skyline built on oil money.",
        "faqItems": [
            {"q": "Is the Sixth Floor Museum at Dealey Plaza worth visiting?", "a": "Yes — the Sixth Floor Museum is one of the best history museums in the US. It occupies the 6th floor of the Texas School Book Depository where Lee Harvey Oswald fired on President Kennedy in 1963. The exhibits are thoughtful and comprehensive. The view from the window where the shots were fired is genuinely affecting. Buy tickets online."},
            {"q": "What is Deep Ellum?", "a": "Deep Ellum is Dallas's historic arts and music district east of downtown — a grid of 1900s commercial buildings now housing live music venues, bars, restaurants, and galleries. The area was the center of Texas blues in the 1920s and 1930s (Blind Lemon Jefferson, Leadbelly). Today it's the most vibrant nightlife district in Dallas."},
            {"q": "What is the difference between Dallas and Fort Worth?", "a": "Dallas and Fort Worth are 30 miles apart and often grouped as the 'Metroplex.' Dallas is the business and arts center — gleaming glass towers, the arts district, corporate headquarters. Fort Worth is authentically Western — the Stockyards National Historic District, rodeos, Western wear shops, and a genuine cowboy culture. Do both if you can."},
            {"q": "What are the best restaurants in Dallas?", "a": "Uchi Dallas for Japanese-inspired fine dining. Pecan Lodge in Deep Ellum for Dallas's best BBQ. Sachet in Knox-Henderson for Mediterranean. Niwa for Japanese beef. The Indian food in Irving (Dallas suburb) — particularly along Esters Road — is among the best in the South."},
            {"q": "What is the Dallas Arts District?", "a": "The Dallas Arts District is the largest urban arts district in the US — a 68-acre stretch north of downtown with the Dallas Museum of Art (free admission), the Nasher Sculpture Center (Renzo Piano building, world-class collection), the AT&T Performing Arts Center, and the Meyerson Symphony Center."},
            {"q": "When is the best time to visit Dallas?", "a": "March–May and October–November. Dallas summers are extremely hot (100°F+) and humid. The State Fair of Texas (3 weeks in October) at Fair Park is the biggest state fair in the US by attendance."},
            {"q": "How do I get from Dallas to Fort Worth?", "a": "Trinity Railway Express (TRE) commuter rail runs between Dallas Union Station and Fort Worth T&P Station — 1 hour, $5. The DART light rail in Dallas also connects to TRE. Easy day trip in either direction."},
            {"q": "What is the Dallas Museum of Art?", "a": "The Dallas Museum of Art has one of the best collections in the South — strong in pre-Columbian art, American art, and contemporary work. Free general admission. The building (designed by Edward Larrabee Barnes) is attractive. The Nasher Sculpture Center next door (Renzo Piano) has an extraordinary collection of 20th-century sculpture in an outdoor garden setting."},
        ],
        "affiliatePicks": [
            {"name": "The Joule Dallas", "type": "hotel", "url": "https://www.booking.com/hotel/us/the-joule.html?aid=2778866", "description": "Dallas's best boutique hotel — Gothic Revival skyscraper with a famous cantilevered rooftop pool over Main Street.", "priceRange": "$$$$"},
            {"name": "Sixth Floor Museum at Dealey Plaza Tickets", "type": "activity", "url": "https://www.getyourguide.com/dallas-l193/?partner_id=IVN6IQ3&q=Sixth+Floor+Museum+JFK", "description": "Advance tickets for the JFK assassination museum — skip the line with reserved entry.", "priceRange": "$"},
            {"name": "Dallas Food and Deep Ellum Tour", "type": "tour", "url": "https://www.getyourguide.com/dallas-l193/?partner_id=IVN6IQ3&q=Dallas+food+tour+Deep+Ellum", "description": "Guided food and neighborhood tour through Deep Ellum and Dallas's restaurant scene.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Dallas/Fort Worth International (DFW) is one of the largest airports in the world — plan extra time for connections. DART light rail Orange Line runs from DFW to downtown Dallas. Domestic Love Field (DAL, Southwest hub) is closer to downtown.",
            "bestTime": "March–May and October–November. October brings the State Fair of Texas. March is warm and less crowded than summer.",
            "gettingAround": "DART light rail covers the Arts District, Deep Ellum, and connections to DFW. Car necessary for broader Dallas exploration. TRE rail to Fort Worth is excellent.",
            "money": "Dallas has a wide range of hotel options — $120–200/night for solid mid-range. The Dallas Museum of Art is free. Arts District and Deep Ellum restaurants run $20–50/person.",
            "safety": "Deep Ellum and the Arts District are safe tourist areas with active foot traffic. Downtown Dallas has some empty blocks at night — stick to the active zones.",
            "packing": "Business casual for arts district evenings. Comfortable shoes for Deep Ellum walking. Sun protection for the heat.",
            "localCulture": "Dallas has a palpable ambition — the city is proud of its growth and transformation. The arts scene is taken seriously. Football (Cowboys) is genuinely quasi-religious. The 'Big D' identity blends genuine Texas pride with cosmopolitan aspirations."
        },
    },
    "big-bend": {
        "description": "Big Bend National Park is the most remote and least visited of Texas's national parks — 800,000 acres on the Rio Grande border with Mexico, with desert canyons, Chisos Mountains, hot springs, and exceptional dark skies.",
        "tagline": "Where the Rio Grande bends",
        "region": "west-texas",
        "aeo": "Big Bend National Park is one of the most remote and least visited national parks in the contiguous US — 801,000 acres of Chihuahuan Desert on the Rio Grande border with Mexico, with three environments (desert floor, Chisos Mountains rising to 7,825 feet, and the river canyon), extraordinary dark skies for stargazing, and a solitude that's increasingly rare in national parks.",
        "gradient": "linear-gradient(135deg, #dc2626, #92400e, #1c1917)",
        "video_title": "Big Bend: Where the River Bends",
        "video_text": "800,000 acres. The Rio Grande. The darkest skies in Texas.",
        "faqItems": [
            {"q": "How far is Big Bend from anywhere?", "a": "Very far. Big Bend is approximately 6 hours from San Antonio, 8 hours from Dallas, and 3 hours from El Paso. The town of Terlingua (just outside the park) and Marathon (40 miles north) are the nearest services. Midland/Odessa (3.5 hours) has the nearest major airport with direct flights from Dallas and Houston. Gas is available in Terlingua and Marathon — fill up."},
            {"q": "What are the must-do activities at Big Bend?", "a": "Santa Elena Canyon (3-mile round trip on the Rio Grande, 1,500-foot canyon walls above you), the Window Trail (5.6 miles round trip, dramatic views from the Chisos Basin), Boquillas Canyon hot springs, and the Lost Mine Trail (4.8 miles, Chisos Mountain views). Stargazing from anywhere — Big Bend is one of the darkest places in the lower 48."},
            {"q": "When is the best time to visit Big Bend?", "a": "October–April. Summer (May–September) is extremely hot — desert floor temperatures exceed 110°F regularly. The Chisos Mountains are significantly cooler (70–80°F) but still warm. Spring wildflowers (February–April) are extraordinary in good rain years. Fall is excellent for desert hiking."},
            {"q": "Where do I stay near Big Bend?", "a": "Chisos Mountains Lodge is the only lodging inside the park (book 6+ months ahead — very limited availability). Outside the park: Terlingua (ghost town turned community of artists, guides, and eccentrics), Marathon (70 miles north, with the historic Gage Hotel), and the Lajitas Golf Resort (luxury option on the river)."},
            {"q": "Is Big Bend safe?", "a": "Yes, with standard national park precautions. The desert heat is the primary danger — carry 1 gallon of water per person per day for summer hiking. Border crossing into Boquillas, Mexico (via rowboat) is legal with a passport and customs registration. Do not cross the border at any other point."},
            {"q": "What is the Marfa connection?", "a": "Marfa (3 hours from Big Bend via Alpine) is a famous West Texas arts community known for the Marfa Lights (unexplained lights visible from a highway viewpoint east of town) and the Chinati Foundation (Donald Judd's massive installation art complex). It makes an excellent addition to a Big Bend road trip."},
            {"q": "Do I need 4WD at Big Bend?", "a": "Many backcountry roads (River Road, Old Maverick Road) require high-clearance 4WD, especially after rain. Paved roads to the Chisos Basin, Santa Elena Canyon, and Boquillas Canyon are accessible by standard vehicles. Check road conditions at the visitor center — conditions change fast."},
            {"q": "What is the Boquillas crossing?", "a": "Boquillas del Carmen is a small Mexican village across the Rio Grande, accessible by rowboat ($5 cash) from the Boquillas Canyon trailhead. You can visit the village, eat at the restaurant, and return to the US — a fascinating cross-border experience. Bring your passport and register with US Customs before crossing (there's a self-service kiosk at the crossing point)."},
        ],
        "affiliatePicks": [
            {"name": "Chisos Mountains Lodge", "type": "hotel", "url": "https://www.booking.com/hotel/us/chisos-mountains-lodge.html?aid=2778866", "description": "The only lodging inside Big Bend — basic rooms and cabins in the Chisos Basin. Book 6+ months ahead.", "priceRange": "$$"},
            {"name": "Big Bend Guided Canyon Canoe/Kayak Tour", "type": "tour", "url": "https://www.getyourguide.com/big-bend-national-park-l107/?partner_id=IVN6IQ3&q=Big+Bend+Rio+Grande+canoe", "description": "Guided multi-day canoe trip through Santa Elena or Boquillas Canyon on the Rio Grande.", "priceRange": "$$$"},
            {"name": "Big Bend Star Party Guided Stargazing", "type": "activity", "url": "https://www.getyourguide.com/big-bend-national-park-l107/?partner_id=IVN6IQ3&q=Big+Bend+stargazing", "description": "Guided stargazing event at Big Bend — some of the darkest skies in the lower 48 states.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Plan 3-4 days minimum — it's too far to rush. Fly into Midland/Odessa (MAF, 3.5 hrs from the park) or El Paso (ELP, 3 hrs) from Dallas or Houston. Rent a car. Fill gas at Terlingua and Marathon — no services inside the park except the Basin store.",
            "bestTime": "October–April. The Chisos Mountains are cooler in summer but still hot on the desert floor. February–March has wildflowers. November–January has the best conditions for extended desert hiking.",
            "gettingAround": "Car essential — the park is 70 miles end to end. Most paved roads accessible by standard vehicle. Fill your gas tank daily at Terlingua — desert driving burns gas.",
            "money": "$35/vehicle park entry (7 days). Chisos Mountains Lodge runs $150–200/night. Terlingua lodging (Starlight Theatre, Big Bend Resort) runs $100–180/night. Budget for gas — distances are extreme.",
            "safety": "Desert heat is the primary danger — carry a gallon of water per person per day. Desert flash floods in canyon areas during monsoon (July–September). Bear safety required in the Chisos Mountains — store food in bear boxes.",
            "packing": "Large water supply (2 gallons per person for a full day is not excessive). Sun protection — UV is extreme at altitude and elevation. Stargazing equipment. Good hiking boots for canyon terrain. Binoculars for wildlife.",
            "localCulture": "Big Bend's remoteness and the Terlingua community (a genuine gathering of desert artists, guides, and eccentrics) create a culture unlike anywhere else in Texas. The Terlingua Chili Championship each November is one of the great Texas events. The border proximity and the ghost town atmosphere of Terlingua are the local flavors."
        },
    },
    "fredericksburg": {
        "description": "Fredericksburg is the Texas Hill Country's most charming small town — a German immigrant settlement from 1846 with excellent wineries, National Museum of the Pacific War, and peach season from June to August.",
        "tagline": "Texas Hill Country's German heart",
        "region": "hill-country",
        "aeo": "Fredericksburg is the Texas Hill Country's most popular small town — a German immigrant community founded in 1846 that's now the center of the Texas wine industry, with 60+ wineries along US-290 (the 'Wine Road'), the exceptional National Museum of the Pacific War (Admiral Chester Nimitz's birthplace), and peach orchards producing the best peaches in Texas each June through August.",
        "gradient": "linear-gradient(135deg, #166534, #92400e, #dc2626)",
        "video_title": "Fredericksburg: Hill Country Wine and History",
        "video_text": "Texas wine, peach season, and Admiral Nimitz's hometown.",
        "faqItems": [
            {"q": "What is the best season to visit Fredericksburg?", "a": "Spring (March–May) for bluebonnets and wildflowers. Summer (June–August) for peach season — the peach stands along US-290 sell fruit so ripe it's worth a trip alone. Fall (September–November) for wine harvest and pleasant temperatures. Wildflower season (late March–late April) draws crowds — book far ahead."},
            {"q": "What are the best wineries near Fredericksburg?", "a": "Becker Vineyards for consistent quality and beautiful grounds. Driftwood Estate for an off-the-beaten-path experience. Kuhlman Cellars for premium small-batch wines. Grape Creek Vineyards for the tuscany-inspired setting. Buy a Texas Wine Trail passport for discounts across the region. The Willow City Loop road (north of town) passes through beautiful Hill Country scenery on the way to wineries."},
            {"q": "What is the National Museum of the Pacific War?", "a": "One of the finest military museums in the US — located in Fredericksburg because Admiral Chester Nimitz, Commander in Chief of Pacific Fleet during WWII, was born here. The museum complex covers the Pacific theater comprehensively, with artifacts, oral histories, and immersive environments. Budget half a day."},
            {"q": "What is Enchanted Rock?", "a": "Enchanted Rock State Natural Area (18 miles north of Fredericksburg) is a massive pink granite dome rising 425 feet above the Hill Country, sacred to the Tonkawa people and now one of the most popular state parks in Texas. Timed entry permits required — reserve on Recreation.gov well in advance."},
            {"q": "What should I eat in Fredericksburg?", "a": "Der Lindenbaum for German schnitzel and sausage (the heritage food). August E's for wine country fine dining. Clear River Pecan for pecan pie. The weekend farmers market on Main Street for local peaches, jams, and artisan goods in season."},
            {"q": "How far is Fredericksburg from Austin and San Antonio?", "a": "Fredericksburg is 80 miles from Austin (1.5 hours) and 80 miles from San Antonio (1.5 hours) — it's equidistant and an easy day trip or overnight from either city. Combining Fredericksburg with Enchanted Rock and Marble Falls makes an excellent Hill Country loop."},
            {"q": "Is Fredericksburg good for families?", "a": "Very good. The National Museum of the Pacific War is excellent for older children. Enchanted Rock has an easy summit trail. The peach stands and wildflower meadows are accessible to all ages. Main Street shopping is family-friendly."},
            {"q": "What is Main Street like in Fredericksburg?", "a": "Fredericksburg's Main Street (Hauptstrasse) is the best-preserved small-town commercial street in Texas — several blocks of 19th-century limestone buildings with wine tasting rooms, antique shops, boutiques, bakeries, and restaurants. Weekend pedestrian traffic can be intense but the street itself is genuinely historic."},
        ],
        "affiliatePicks": [
            {"name": "Fredericksburg Inn and Suites", "type": "hotel", "url": "https://www.booking.com/city/us/fredericksburg-tx.html?aid=2778866", "description": "Well-located Fredericksburg lodging — book well ahead for spring wildflower season.", "priceRange": "$$"},
            {"name": "Texas Wine Trail Winery Tour", "type": "tour", "url": "https://www.getyourguide.com/fredericksburg-l4474/?partner_id=IVN6IQ3&q=Fredericksburg+wine+tour", "description": "Guided Hill Country wine tour covering 3-4 vineyards with transportation from Fredericksburg.", "priceRange": "$$"},
            {"name": "Enchanted Rock Hiking Permit", "type": "activity", "url": "https://www.getyourguide.com/fredericksburg-l4474/?partner_id=IVN6IQ3&q=Enchanted+Rock+hiking", "description": "Reserve timed entry permits for Enchanted Rock State Natural Area — sells out fast.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Fredericksburg is best done as an overnight stay, not a day trip — the wineries benefit from unhurried afternoon visits. Book accommodations well ahead for March–April wildflower season and September–November harvest season. US-290 east toward Austin is the Wine Road.",
            "bestTime": "Late March–April for bluebonnets and wildflowers (the wildflower drive on US-290 is spectacular). June–August for peach season. September–November for wine harvest.",
            "gettingAround": "Car essential — the wineries are spread along US-290 over 20 miles. Designated driver or hire a wine tour guide for the full circuit.",
            "money": "Moderate to upscale. Winery tastings run $10–20 per flight. Hotels in peak season (wildflower, harvest) run $150–250/night. National Museum of the Pacific War is $16/adult.",
            "safety": "Designated driver for the wine trail — the Hill Country roads are narrow and winding.",
            "packing": "Wine tasting-appropriate clothing. Hat and sunscreen for outdoor winery visits. Camera for wildflowers and the Hill Country landscape.",
            "localCulture": "Fredericksburg's German heritage is genuine — the limestone architecture, the 'Wurst Fest' in November, and the food traditions go back to the 1846 settlers. The wine industry has added a new identity that blends surprisingly well with the pioneer history."
        },
    },
    "marfa": {
        "description": "Marfa is West Texas's art world outpost — a tiny high-desert city with Donald Judd's permanent art installations at the Chinati Foundation, the mysterious Marfa Lights, and an art scene that draws international visitors.",
        "tagline": "West Texas art world in the desert",
        "region": "west-texas",
        "aeo": "Marfa is one of America's most improbable cultural destinations — a West Texas cattle town of 1,900 people at 4,688 feet elevation that became an internationally recognized arts destination when sculptor Donald Judd moved here in 1971 and installed 100 aluminum boxes and 15 concrete artillery sheds that are now the Chinati Foundation. The Marfa Lights (unexplained lights visible from the highway east of town) add mystique to what is already a singular place.",
        "gradient": "linear-gradient(135deg, #1c1917, #7c3aed, #dc2626)",
        "video_title": "Marfa: Art in the Desert",
        "video_text": "Donald Judd, the Marfa Lights, and a cattle town turned art world.",
        "faqItems": [
            {"q": "What is the Chinati Foundation?", "a": "The Chinati Foundation is Donald Judd's permanently installed art complex in the old Fort D. A. Russell military base outside Marfa. The centerpiece is 100 untitled works in mill aluminum (1982-1986) in two repurposed artillery sheds — the light changes throughout the day, altering how the aluminum catches and reflects it. Also on the grounds: John Chamberlain's crushed car sculptures and Dan Flavin's fluorescent light installations. The most important contemporary art destination in Texas."},
            {"q": "What are the Marfa Lights?", "a": "The Marfa Lights are unexplained lights visible from a roadside viewing platform east of town on US-90, typically appearing after dark as moving, splitting, and merging colored lights on the horizon. The scientific explanation is atmospheric refraction of car headlights and other light sources, but their behavior has never been fully explained. The viewing platform is free; the lights appear most frequently in dry weather."},
            {"q": "Is Marfa worth the drive?", "a": "If art matters to you, absolutely. The Chinati Foundation is a once-in-a-lifetime art experience that can't be replicated. If you're primarily drawn by the Instagram aesthetic, it's worth knowing Marfa is genuinely remote and requires commitment. The drive from Alpine (30 miles) or Big Bend (3 hours) makes it most logical as part of a West Texas trip."},
            {"q": "When should I visit the Chinati Foundation?", "a": "Wednesday–Sunday, 9am–5pm, by tour only ($25/adult, guided tours run 3 hours). The foundation is closed Monday and Tuesday. Reserve tours in advance at chinati.org — limited capacity. The Open House weekend (one weekend per year in October) allows extended access and draws large crowds."},
            {"q": "What else is there to do in Marfa?", "a": "The Judd Foundation (separate from Chinati) preserves Donald Judd's personal living and studio spaces in the Lobo lofts and Block. El Cosmico campsite and hotel is a design-forward glamping experience. The Marfa Book Company is one of the best independent bookstores in Texas. Ballroom Marfa hosts rotating contemporary art exhibitions."},
            {"q": "Where do I eat in Marfa?", "a": "Cochineal for the best fine dining (reservation essential, often booked weeks ahead). Lost Horse Saloon for drinks and live music. Food Shark for the outdoor lunch truck (Wednesdays–Saturdays). The Padre Hotel has a good bar."},
            {"q": "How do I get to Marfa?", "a": "Marfa is 196 miles from El Paso (3 hours), 233 miles from San Antonio (3.5 hours), and 350+ miles from Dallas and Austin. The nearest commercial airports are Midland/Odessa (MAF, 2.5 hours) and El Paso (ELP, 3 hours). Rent a car — no public transportation reaches Marfa."},
            {"q": "What is El Cosmico?", "a": "El Cosmico is a design-forward campsite and hotel in Marfa — trailers, yurts, and teepees set on a 21-acre property with a communal kitchen and saltwater pool. It's become as much a destination as the art, with a particular appeal to design-minded travelers. Book well ahead — limited inventory."},
        ],
        "affiliatePicks": [
            {"name": "Hotel Saint George Marfa", "type": "hotel", "url": "https://www.booking.com/hotel/us/hotel-saint-george-marfa.html?aid=2778866", "description": "The best hotel in Marfa — modernist design, gallery-quality art throughout, excellent restaurant.", "priceRange": "$$$"},
            {"name": "Chinati Foundation Tour", "type": "tour", "url": f"{GYG}&q=Chinati+Foundation+Marfa+art+tour", "description": "Reserve guided tours of the Chinati Foundation — Donald Judd's permanent art installation.", "priceRange": "$$"},
            {"name": "Marfa Lights and West Texas Tour", "type": "tour", "url": f"{GYG}&q=Marfa+Texas+tour", "description": "Guided Marfa tour covering the Chinati Foundation, Marfa Lights, and desert context.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Marfa is genuinely remote — plan your route carefully. Big Bend (3 hrs south) and Alpine (30 minutes north) are natural pairings. Fly into Midland/Odessa or El Paso and rent a car.",
            "bestTime": "October–April for the most comfortable temperatures. October's Chinati Open House brings the largest crowds (and most exciting programming) of the year. Summers are hot but the altitude (4,688 ft) keeps it cooler than the desert floor.",
            "gettingAround": "Marfa itself is walkable for the downtown galleries and restaurants. Car essential for Chinati Foundation (a few miles from downtown) and Big Bend/other destinations.",
            "money": "Marfa is surprisingly expensive for a small town — the art world clientele drives pricing. Hotels run $150–300/night. Dinners at Cochineal run $60–80/person. The Chinati Foundation tour is $25.",
            "safety": "Marfa itself is very safe. Driving between Marfa and other West Texas destinations involves long, empty highways — watch for deer especially at dawn/dusk.",
            "packing": "Layers for the altitude — Marfa nights are cool even in summer. Camera for the Chinati Foundation spaces (photography allowed in most areas). Comfortable shoes for walking the foundation grounds.",
            "localCulture": "Marfa's combination of authentic West Texas cattle culture and imported New York/LA art world creates a surreal but genuine social mix. The locals are generally welcoming of visitors who engage respectfully. The Instagram crowd is noticed and tolerated. The art is serious."
        },
    },
}

# Minimal data for remaining destinations
REMAINING_SLUGS = [
    "abilene", "alpine", "amarillo", "bandera", "boerne", "brownsville",
    "bryan-college-station", "caddo-lake", "canyon", "corpus-christi",
    "del-rio", "denton", "dripping-springs", "eagle-pass", "el-paso",
    "enchanted-rock", "fort-worth", "galveston", "georgetown", "glen-rose",
    "granbury", "grapevine", "guadalupe-mountains", "jefferson", "johnson-city",
    "kerrville", "killeen", "kingsville", "laredo", "lubbock", "luckenbach",
    "lufkin", "marble-falls", "matagorda", "mcallen", "mckinney",
    "midland-odessa", "nacogdoches", "new-braunfels", "palo-duro-canyon",
    "port-aransas", "port-isabel", "rockport-fulton", "round-rock",
    "san-marcos", "south-padre-island", "surfside-beach", "temple-belton",
    "terlingua", "tyler", "waco", "wimberley"
]

# Generic stub template for remaining destinations
STUB_DEFAULTS = {
    "gradient": "linear-gradient(135deg, #dc2626, #92400e, #1e40af)",
    "video_title": "Discover Texas",
    "video_text": "The Lone Star State. Everything is bigger here.",
    "faqItems": [
        {"q": "When is the best time to visit?", "a": "Spring (March-May) and fall (October-November) offer the most comfortable temperatures for outdoor activities across most of Texas. Summer heat can be extreme — plan outdoor activities for early morning."},
        {"q": "Do I need a car?", "a": "Yes — a car is essential for almost all Texas destinations outside of downtown Houston, Dallas, and Austin. The distances between attractions are significant."},
        {"q": "What is Texas weather like?", "a": "Hot and variable. Most of Texas experiences hot summers (95-105°F), mild winters, and dramatic weather swings including thunderstorms. The Gulf Coast gets hurricanes in summer/fall; West Texas is dry desert; East Texas is humid subtropical."},
        {"q": "What is the local food like?", "a": "Texas cuisine varies by region — BBQ in Central Texas, Tex-Mex and Mexican-American food throughout, Gulf seafood on the coast, and fusion cuisine in the major cities. Each region has distinct culinary traditions worth exploring."},
        {"q": "How do I get around Texas efficiently?", "a": "Fly between cities — Texas is enormous. Dallas-Houston-San Antonio-Austin form the main travel triangle. Driving between any two major cities takes 3-5 hours. Southwest Airlines has excellent intra-Texas coverage."},
        {"q": "What makes Texas special?", "a": "Texas has a distinct cultural identity — a blend of Southern, Mexican, and Western traditions that's unlike any other US state. The pride in Texas identity is genuine and pervasive."},
        {"q": "Is Texas good for outdoor adventures?", "a": "Excellent — Big Bend National Park, Enchanted Rock, Guadalupe Mountains, Padre Island National Seashore, and the Hill Country provide outstanding outdoor experiences across diverse environments."},
        {"q": "What are the Texas state parks like?", "a": "Texas state parks are generally excellent and affordable. The Lone Star Land Steward Pass ($70/year) covers most state park entry fees and is worth purchasing for a multi-destination Texas trip."},
    ],
    "affiliatePicks_generic": [
        {"name": "Texas State Park Hotels", "type": "hotel", "url": f"{BOOKING}&ss=Texas", "description": "Find accommodations near Texas destinations.", "priceRange": "$$"},
        {"name": "Texas Guided Day Tour", "type": "tour", "url": f"{GYG}&q=Texas+guided+tour", "description": "Discover local highlights with an experienced guide.", "priceRange": "$$"},
        {"name": "Texas Travel Guide", "type": "activity", "url": f"{AMAZON}&k=texas+travel+guide", "description": "Comprehensive Texas travel guide for planning your trip.", "priceRange": "$"},
    ],
    "scottTips_generic": {
        "logistics": "Texas is large — fly between major cities rather than driving. Southwest Airlines has excellent intra-Texas routes. A car is essential once you arrive.",
        "bestTime": "March-May and October-November for the most comfortable outdoor temperatures. Summer heat (95-105°F+) limits midday outdoor activities.",
        "gettingAround": "Car essential for all Texas travel outside major city centers. Distances are significant — plan driving time carefully.",
        "money": "Texas has no state income tax, which contributes to generally affordable pricing for dining and activities. Hotels range widely by location and season.",
        "safety": "Texas is generally safe for tourists in established destinations. Summer heat is the primary safety concern — carry water and limit outdoor exposure at midday.",
        "packing": "Light clothing for the heat. Layers for air-conditioned interiors. Sun protection year-round. Good walking shoes.",
        "localCulture": "Texas pride is genuine and pervasive — locals are proud of their state's scale, history, and culture. The BBQ, Tex-Mex, and live music traditions are living culture, not tourist performance."
    },
}

FRONTMATTER_CLOSE = "contentStatus: draft\ndraft: false"

def build_faqItems_yaml(faqItems):
    yaml = "faqItems:\n"
    for faq in faqItems:
        q = faq['q'].replace('"', "'")
        a = faq['a'].replace('"', "'")
        yaml += f'  - question: "{q}"\n    answer: "{a}"\n'
    return yaml

def build_affiliatePicks_yaml(affiliatePicks):
    yaml = "affiliatePicks:\n"
    for pick in affiliatePicks:
        yaml += f"""  - name: "{pick['name']}"
    type: {pick['type']}
    url: "{pick['url']}"
    description: "{pick['description']}"
    priceRange: "{pick['priceRange']}"
"""
    return yaml

def build_scottTips_yaml(scottTips):
    return f"""scottTips:
  logistics: "{scottTips.get('logistics', '').replace('"', "'")}"
  bestTime: "{scottTips.get('bestTime', '').replace('"', "'")}"
  gettingAround: "{scottTips.get('gettingAround', '').replace('"', "'")}"
  money: "{scottTips.get('money', '').replace('"', "'")}"
  safety: "{scottTips.get('safety', '').replace('"', "'")}"
  packing: "{scottTips.get('packing', '').replace('"', "'")}"
  localCulture: "{scottTips.get('localCulture', '').replace('"', "'")}"
"""

def process_file(filepath, slug, faqItems, affiliatePicks, scottTips, aeo, gradient, video_title, video_text):
    content = open(filepath, 'r', encoding='utf-8').read()

    if "scottTips:" in content:
        print(f"SKIP {slug} — already done")
        return

    new_fm = build_faqItems_yaml(faqItems) + build_affiliatePicks_yaml(affiliatePicks).rstrip() + "\n" + build_scottTips_yaml(scottTips) + "contentStatus: published\ndraft: false"
    content = content.replace(FRONTMATTER_CLOSE, new_fm)

    # Add AEO and video block to body
    video_block = f"""<div class="immersive-break-inline">
  <video autoplay muted loop playsinline preload="metadata">
    <source src="/videos/destinations/{slug}-hero.mp4" type="video/mp4" />
  </video>
  <div class="ib-gradient" style="background: {gradient};"></div>
  <div class="ib-content">
    <div class="ib-title">{video_title}</div>
    <p class="ib-text">{video_text}</p>
  </div>
</div>"""

    lines = content.split('\n')
    fm_count = 0
    fm_end = -1
    for i, line in enumerate(lines):
        if line.strip() == '---':
            fm_count += 1
            if fm_count == 2:
                fm_end = i
                break

    if fm_end >= 0:
        body_lines = lines[fm_end+1:]
        first_para_end = -1
        in_para = False
        for j, bl in enumerate(body_lines):
            if bl.strip() and not in_para:
                in_para = True
            elif not bl.strip() and in_para:
                first_para_end = j
                break

        if first_para_end >= 0:
            new_body_lines = []
            if aeo:
                new_body_lines.append(aeo)
                new_body_lines.append("")
            new_body_lines.extend(body_lines[:first_para_end])
            new_body_lines.append("")
            new_body_lines.append(video_block)
            new_body_lines.append("")
            new_body_lines.extend(body_lines[first_para_end:])
            content = '\n'.join(lines[:fm_end+1]) + '\n' + '\n'.join(new_body_lines)

    open(filepath, 'w', encoding='utf-8').write(content)
    print(f"Done {slug}")


# Process priority destinations
for slug, data in PRIORITY.items():
    filepath = f"{BASE}/{slug}.md"
    if not os.path.exists(filepath):
        print(f"SKIP {slug} — not found")
        continue
    process_file(
        filepath, slug,
        data.get("faqItems", STUB_DEFAULTS["faqItems"]),
        data.get("affiliatePicks", STUB_DEFAULTS["affiliatePicks_generic"]),
        data.get("scottTips", STUB_DEFAULTS["scottTips_generic"]),
        data.get("aeo", ""),
        data.get("gradient", STUB_DEFAULTS["gradient"]),
        data.get("video_title", STUB_DEFAULTS["video_title"]),
        data.get("video_text", STUB_DEFAULTS["video_text"]),
    )

# Process remaining stubs with generic data
for slug in REMAINING_SLUGS:
    filepath = f"{BASE}/{slug}.md"
    if not os.path.exists(filepath):
        print(f"SKIP {slug} — not found")
        continue
    content_check = open(filepath, 'r', encoding='utf-8').read()
    if "scottTips:" in content_check:
        print(f"SKIP {slug} — already done")
        continue

    # Customize gradient per region
    gradient = STUB_DEFAULTS["gradient"]
    if slug in ["port-aransas", "south-padre-island", "galveston", "corpus-christi", "port-isabel", "matagorda", "surfside-beach", "rockport-fulton", "brownsville"]:
        gradient = "linear-gradient(135deg, #0369a1, #0ea5e9, #166534)"
    elif slug in ["amarillo", "lubbock", "canyon", "palo-duro-canyon", "midland-odessa"]:
        gradient = "linear-gradient(135deg, #92400e, #dc2626, #b45309)"
    elif slug in ["el-paso", "guadalupe-mountains", "terlingua", "alpine"]:
        gradient = "linear-gradient(135deg, #dc2626, #92400e, #1c1917)"
    elif slug in ["caddo-lake", "nacogdoches", "lufkin", "jefferson", "tyler"]:
        gradient = "linear-gradient(135deg, #166534, #15803d, #92400e)"

    process_file(
        filepath, slug,
        STUB_DEFAULTS["faqItems"],
        STUB_DEFAULTS["affiliatePicks_generic"],
        STUB_DEFAULTS["scottTips_generic"],
        "",  # No custom AEO for stubs
        gradient,
        "Discover Texas",
        "The Lone Star State. Everything is bigger here.",
    )

print("Texas Tier 3 complete")
