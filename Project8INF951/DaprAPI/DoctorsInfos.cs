using System.ComponentModel.DataAnnotations;

namespace DaprAPI
{
    public class DoctorsInfos
    {
        public string? Nom { get; set; }
        public string? Prenom { get; set; }
        public string? Ville { get; set; }
        
        public DateTime Dob { get; set; }
       
        public string? Email { get; set; }

        public DateTime Date { get; set; }

    }
}