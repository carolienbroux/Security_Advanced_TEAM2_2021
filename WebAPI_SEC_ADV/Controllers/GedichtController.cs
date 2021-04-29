using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace WebAPI_SEC_ADV.Controllers
{
    [Route("api/Gedicht")]
    [ApiController]
    public class GedichtController : ControllerBase
    {
        [HttpGet]
        [Authorize]
        public ActionResult<List<string>> GetGedicht()
        {
            return Ok( new List<string>()
            {
                "Doe gewoon eens gek",
                "Spring uit de ban",
                "Maak uitbundig plezier",
                "En geniet ervan"
            });
        }
    }
}
