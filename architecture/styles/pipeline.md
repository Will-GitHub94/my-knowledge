# Pipeline *(Pipe and Filter)*

<img src="../assets/pipes-and-filters.png"/>

***

### Overview

+ Has routes at a very very low level *(OS level typically)*
+ Conists of 2 types of components:
  1. **Filters**: Receives data...does something with it and then pushes it on to the next *Filter*
  2. **Pipes**: Connects various *Filter*s and transfers data to those *Filter*s

***

### Components

#### Pipes

<img src="../assets/pipes.png" style="width: 200px"/>

+ Unidirectional **only** *(Fire & Forget)*
+ Usually point-to-point for high performance, but could be message-based for scalability
+ Payload *(carries data from 1 filter to another)* can be any types (text, bytes, object...)

***

#### Filters

<img src="../assets/filters.png" style="width: 200px"/>

+ Self-contained and independent *(no cohesion)* from other *Filter*s
+ Usually designed to perform a single specific task
+ 4 types:
  1. **Producer**: _Starting point, outbound **only**_
  					<img src="../assets/producer.png" style="width: 100px"/>
  2. **Consumer**: _Ending point, inbound **only**_
  					<img src="../assets/consumer.png" style="width: 100px"/>
  3. **Transformer**: _Input, processing, output_
  					<img src="../assets/transformer.png" style="width: 100px"/>
  4. **Tester**: _Input, discard/pass-thru_
  					<img src="../assets/tester.png" style="width: 100px"/>

***

### Notes

This pattern looks similar to event-driven in the way that *Filter*s recieve data, process it, and then pass it along... much like what *Process*es do in an EDA.<br>However, even though these look the same they are very different...

| Pipes & Filters                 | Event-Driven                       |
|:-------------------------------:|:----------------------------------:|
| Synchronous data filtering      | Asynchronous Event Processing      |
| Single target for *Pipe*s       | Multiple targets for *Event*       |
| Simple single purpose *Filter*s | Complex multi-purpose *Processor*s |

### Considerations

+ Useful for smaller deterministic systems with a distinct processing flow
  <small><i>"I do this, then I do this, then I do this"</i></small>
+ *Filter*s can easily be added & removed
+ Provides for a high level of decoupling
+ Supports Evolutionary Design
  <small><i>If you don't have all the requirements at project start, great! Can continue to add and evolve the pattern as business needds are determined</i></small>
+ Able to easily adapt to changing requirements
+ Can be easily incorporated into another pattern
  <small><i>For example, can have a Pipe & Filter mechanism within a microservice</i></small>
+ Due to *Filter*s being small, they are often reuseable