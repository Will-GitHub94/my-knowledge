# Software Architecure

### Description

Software Architecture is the *blueprint* of a sytstem. It will define such things as:

- Performance
- Modifiability
- Security

I see it as the structure of a system and **does not** define technologies used. For example, you may say that we are using an MV* architecture, but nowhere in the report should you mention that we are using Angular2 for this...

Software Architecture defines the relationships of elements within a system

> *"What is software design?"*<br>"The final goal of any engineering activity is some type of documentation (*blueprint*)" - (Reeves, 1992)

In manufacturing world, using atoms which are very hard to change but in software, dealing with bits which are very maluable

Software Manufactuing = Compilation/Deployment

Design Document (blueprint) = Source Code

> "Given that software designs are relatively easy to turn out and essentially free to build, an unsurprising revelation is that software designs tend to be incredibly large and complex" - *(Reeves, 1992)*

For example, in traditional manufacturing, have to make sure that loads of money thrown into it to make it secure as it would be too ridiculous to watch a heavy vehicle roll over a bridge and watch it collapse and then go "well we need to build a better bridge next time". In software, tests/changes are incredibly cheap.

***

### Physical Constraints

##### Traditional manufacturing

Take this electrical socket cover ![alt text](assets/electrical-socket-cover.jpg "Electrical socket Cover")<br>If that cover does not completely cover the whole in the wall, then nothing drastic will happen to the overall architecture of the building.

##### Software

In the software world (in terms of compilation), 1 wrong piece of code can make the code not compile & kill the project so our tolerance for errors is small compared to the real world.

***

### Cause & Effect

##### Traditional manufacturing

If a wing fell off of an aeroplane, you would probably go to the place on the plane where it fell off to try and figure it out

##### Software

You can call some instability to happen that won't manifest for hundreds of lines of codes so is very hard to track down where the problem might lie

***

### Economy & Scale

##### Traditional manufacturing
In the golden gate bridge, there are more 1 million+ rivets & people who understand structural integrity of bridges will be able to tell you what each one is for.

##### Software
May have hundreds/thousands little pieces *(components)* but each 1 of them is a handcrafted little piece *(little or no commonality)* so do not have same level of componentisation that the real world has.


In traditional manufacturing, many hours/lots of money goes into predictability to try and ensure that the thing does what it is supposed to do. That is not required in software world as *(compilation is so cheap)* we would be better off writing tests for the code we write...

**Testing = engineering rigor in software**

> "Software may be cheap to build, but it is *incredibly* expensive to design" - *(Reeves, 1992)*

***

#### Architectural Styles

These tell us, in broad terms, how to organise our code. It is the highest level of granularity & specifies:

  - Layers
  - High-level modules
  - Relationships between modules & layers

Examples of styles are:

  - Component-based
  - Monolithic application
  - Layered
  - Pipes & Filters
  - Event-driven
  - Publish-subscribe
  - Plugins
  - Client-server
  - Service-oriented

Style can be implemented in various ways, with specific technical environment, specific policies, frameworks or practices


#### Architectural Patterns

Pattern is a recurring solution to a recurring problem. In the case of Architectural Patterns, they solve the problems related to the Architectural Style. I.e:

> *"What classes will we have and how will they interact, in order to implement a system with a specific set of layers?""
> *"What high-level modules will we have in our Service-Oriented Architecture and how will they communicate?"*
> *"How many tiers will our Client-Server Architecture have?"*

Patterns have an extensive impact on the code base, most often impacting the whole application either horizontally *(i.e. how to structure the code inside a layer)* or vertically *(i.e. how a request is processed from the outer layers into the inner layers and back)*.

Example of patterns are:

- Three-tier
- Microkernel
- MVC *(Model View Controller)*
  <small><i>Solves the problem of separating UI from the model</i></small>
- MVVM *(Model View View-Model)*