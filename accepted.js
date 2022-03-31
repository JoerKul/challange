Console.WriteLine(Decode("150-177-154-156-149-223-157-144-197-223-214"));

string Decode(string scrambled)
{
  // decode and return the message here
  var decoded = scrambled.split("-").map( item => parseInt(255) - parseInt(item)).map(item => String.fromCharCode(item)).swap();
}

Array.prototype.swap = function () {
    for(var i = 0; i < this.length -1; i++) {
        var t = this[i];
        this[i] = this[i +1];
        this[i+1] = t;  
        i++;
    }
    return this;
}
