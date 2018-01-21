# Microkernel

*Plug-in architecture*


<img src="../assets/microkernal.png"/>

![core]
Smallest possible amount of minimal functionality to run a system.<br>
<small><i>You get it, it's supposed to be small</i></small><br>
Generally only for business rules/business logic.<br>
Generally does not contain any custom processing.<br>

![plugin]
Standalone indpendent modules.<br>
Contain very specific business rules/business logic and **exceptions**<br>
<small><i>Core usually does A, B, C, then D...this custom module does E after C...this is an exception</i></small>

[core]: "../assets/microkernel-core.png"
[plugin]: "../assets/microkernel-plugin.png"

### Example

Eclipse IDE is a *great* example of this architecture.<br>
<img src="../assets/microkernal-eclipse.png"/>

### Considerations

+ Useful for systems that have custom processing or processing that is susceptible to change
+ Plug-in modules can easily be added & removed
+ Supports evolutionary design
+ Easily adapts to any change in requirements
<small><i>If done right, changes should be in plug-in modules so are easily changed</i></small>
+ Easily embeddible into other architecture patterns

