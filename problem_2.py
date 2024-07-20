 protected void Button1_Click(object sender, EventArgs e)
 {
     int decimalNumber;
     bool isNumeric = int.TryParse(TextBox1.Text, out decimalNumber);

     if (!isNumeric || decimalNumber < 0)
     {
         ResultLabel.Text = "Please enter a valid positive decimal number.";
         return;
     }

     string binaryRepresentation = ConvertToBinary(decimalNumber);
     ResultLabel.Text = $"Binary representation: {binaryRepresentation}";
 }

 private string ConvertToBinary(int decimalNumber)
 {
     if (decimalNumber == 0) return "0";

     string binary = string.Empty;

     while (decimalNumber > 0)
     {
         int remainder = decimalNumber % 2;
         binary = remainder + binary;
         decimalNumber /= 2;
     }

     return binary; 
 }
