using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.OpenApi.Writers;


namespace WebAPI_SEC_ADV.Controllers
{
    [ApiController]
    [Route("api/Students")]
    [Authorize]
    public class StudentController : ControllerBase
    {
        [HttpGet]
        
        public ActionResult<List<Student>> GetAll()
        {
            return Ok (new []
            {
                new Student{ Name = "Carolien Broux" },
                new Student{ Name = "Maaike Bex"},
                new Student{ Name = "Stef Brackez"},
                new Student{ Name = "Simon Bovy"}
            });
        }
    }
}
