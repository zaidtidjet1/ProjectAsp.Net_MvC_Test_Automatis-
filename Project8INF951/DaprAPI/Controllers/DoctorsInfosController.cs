using Microsoft.AspNetCore.Mvc;

namespace DaprAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class DoctorsInfosController : ControllerBase
    {
        private static readonly string[] Prénoms = new[]
        {
        "Tidjet", "IAN", "Pilon" };

        private static readonly string[] Noms = new[]
      {
        "Pierre", "Zaid", "Midi" };

        private static readonly string[] Villes = new[]
     {
        "Rimouski", "Matane", "Lévis" };
        private static readonly string[] Emails = new[]
    {
        "allo@gmail.com", "tidz0001@uqar.ca", "Midi@gmail.com" 


    };

        private readonly ILogger<DoctorsInfosController> _logger;

        public DoctorsInfosController(ILogger<DoctorsInfosController> logger)
        {
            _logger = logger;
        }

        [HttpGet(Name = "DoctorsInfos")]
        public IEnumerable<DoctorsInfos> Get()
        {
            return Enumerable.Range(1, 1).Select(index => new DoctorsInfos
            {
                Date = DateTime.Now.AddDays(index),
                Nom = Noms[Random.Shared.Next(Noms.Length)],
                Prenom = Prénoms[Random.Shared.Next(Prénoms.Length)],
                Ville = Villes[Random.Shared.Next(Villes.Length)],
                Email = Emails[Random.Shared.Next(Emails.Length)],

            })
            .ToArray();
        }
        [HttpDelete(Name = "DoctorsInfos")]
        public IEnumerable<DoctorsInfos> Delete()
        {
            return Enumerable.Range(1, 1).Select(index => new DoctorsInfos
            {
                Date = DateTime.Now.AddDays(index),
                Nom = Noms[Random.Shared.Next(Noms.Length)],
                Prenom = Prénoms[Random.Shared.Next(Prénoms.Length)],
                Ville = Villes[Random.Shared.Next(Villes.Length)],
                Email = Emails[Random.Shared.Next(Emails.Length)],

            })
            .ToArray();


        }
        [HttpPut(Name = "DoctorsInfos")]
        public IEnumerable<DoctorsInfos> Put()
        {
            return Enumerable.Range(1, 1).Select(index => new DoctorsInfos
            {
                Date = DateTime.Now.AddDays(index),
                Nom = Noms[Random.Shared.Next(Noms.Length)],
                Prenom = Prénoms[Random.Shared.Next(Prénoms.Length)],
                Ville = Villes[Random.Shared.Next(Villes.Length)],
                Email = Emails[Random.Shared.Next(Emails.Length)],

            })
            .ToArray();


        }
    }
}